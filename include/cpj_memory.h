#ifndef CPJ_MEMORY_H
#define CPJ_MEMORY_H

#include <memory>
#include <atomic>
#include <type_traits>
#include <cassert>
#include <mutex>
#include <unordered_map>
#include <functional>

namespace cpj {
namespace memory {

// Forward declarations
template<typename T> class SafePtr;
template<typename T> class UniquePtr;
template<typename T> class SharedPtr;
template<typename T> class WeakPtr;
template<typename T> class GCPtr;

// Memory tracking for garbage collection
class MemoryTracker {
private:
    static std::unordered_map<void*, size_t> refCounts;
    static std::mutex trackerMutex;
    
public:
    static void increment(void* ptr) {
        std::lock_guard<std::mutex> lock(trackerMutex);
        refCounts[ptr]++;
    }
    
    static void decrement(void* ptr) {
        std::lock_guard<std::mutex> lock(trackerMutex);
        if (--refCounts[ptr] == 0) {
            delete ptr;
            refCounts.erase(ptr);
        }
    }
};

// Base RAII wrapper with safety checks
template<typename T>
class SafePtr {
protected:
    T* ptr;
    std::atomic<bool> valid;
    
    void checkValid() const {
        if (!valid) {
            throw std::runtime_error("Accessing invalid pointer");
        }
    }
    
public:
    SafePtr() : ptr(nullptr), valid(false) {}
    explicit SafePtr(T* p) : ptr(p), valid(p != nullptr) {}
    
    virtual ~SafePtr() {
        valid = false;
    }
    
    T* get() const {
        checkValid();
        return ptr;
    }
    
    T& operator*() const {
        checkValid();
        return *ptr;
    }
    
    T* operator->() const {
        checkValid();
        return ptr;
    }
    
    bool isValid() const { return valid; }
};

// Unique ownership (like C++ std::unique_ptr)
template<typename T>
class UniquePtr : public SafePtr<T> {
public:
    explicit UniquePtr(T* p = nullptr) : SafePtr<T>(p) {}
    
    UniquePtr(UniquePtr&& other) noexcept {
        this->ptr = other.ptr;
        this->valid = other.valid;
        other.ptr = nullptr;
        other.valid = false;
    }
    
    UniquePtr& operator=(UniquePtr&& other) noexcept {
        if (this != &other) {
            delete this->ptr;
            this->ptr = other.ptr;
            this->valid = other.valid;
            other.ptr = nullptr;
            other.valid = false;
        }
        return *this;
    }
    
    ~UniquePtr() {
        delete this->ptr;
    }
    
    // Disable copy
    UniquePtr(const UniquePtr&) = delete;
    UniquePtr& operator=(const UniquePtr&) = delete;
};

// Reference-counted shared ownership (like C++ std::shared_ptr)
template<typename T>
class SharedPtr : public SafePtr<T> {
private:
    std::shared_ptr<T> shared;
    
public:
    explicit SharedPtr(T* p = nullptr) : SafePtr<T>(p), shared(p) {
        this->ptr = shared.get();
    }
    
    SharedPtr(const SharedPtr& other) : SafePtr<T>(other.ptr), shared(other.shared) {
        this->valid = other.valid;
    }
    
    SharedPtr& operator=(const SharedPtr& other) {
        if (this != &other) {
            shared = other.shared;
            this->ptr = shared.get();
            this->valid = other.valid;
        }
        return *this;
    }
};

// Weak reference (like C++ std::weak_ptr)
template<typename T>
class WeakPtr {
private:
    std::weak_ptr<T> weak;
    
public:
    WeakPtr() {}
    WeakPtr(const SharedPtr<T>& shared) : weak(shared.shared) {}
    
    SharedPtr<T> lock() const {
        if (auto shared = weak.lock()) {
            return SharedPtr<T>(shared.get());
        }
        return SharedPtr<T>();
    }
    
    bool expired() const { return weak.expired(); }
};

// Garbage-collected pointer (like Python/Java)
template<typename T>
class GCPtr : public SafePtr<T> {
public:
    explicit GCPtr(T* p = nullptr) : SafePtr<T>(p) {
        if (p) MemoryTracker::increment(p);
    }
    
    GCPtr(const GCPtr& other) : SafePtr<T>(other.ptr) {
        this->valid = other.valid;
        if (this->ptr) MemoryTracker::increment(this->ptr);
    }
    
    GCPtr& operator=(const GCPtr& other) {
        if (this != &other) {
            if (this->ptr) MemoryTracker::decrement(this->ptr);
            this->ptr = other.ptr;
            this->valid = other.valid;
            if (this->ptr) MemoryTracker::increment(this->ptr);
        }
        return *this;
    }
    
    ~GCPtr() {
        if (this->ptr) MemoryTracker::decrement(this->ptr);
    }
};

// Smart factory functions
template<typename T, typename... Args>
UniquePtr<T> makeUnique(Args&&... args) {
    return UniquePtr<T>(new T(std::forward<Args>(args)...));
}

template<typename T, typename... Args>
SharedPtr<T> makeShared(Args&&... args) {
    return SharedPtr<T>(new T(std::forward<Args>(args)...));
}

template<typename T, typename... Args>
GCPtr<T> makeGC(Args&&... args) {
    return GCPtr<T>(new T(std::forward<Args>(args)...));
}

} // namespace memory
} // namespace cpj

#endif // CPJ_MEMORY_H