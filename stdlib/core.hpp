#pragma once

#include <memory>
#include <optional>
#include <variant>
#include <functional>
#include <mutex>

namespace cpj::stdlib {

template<typename T>
class Result {
public:
    Result(T value) : value_(std::move(value)), error_() {}
    Result(std::exception_ptr error) : error_(error) {}
    
    bool isSuccess() const { return !error_; }
    
    T getValue() const {
        if (error_) {
            std::rethrow_exception(error_);
        }
        return value_;
    }

private:
    T value_;
    std::exception_ptr error_;
};

template<typename T>
class Synchronized {
public:
    template<typename F>
    auto with(F func) -> decltype(func(std::declval<T&>())) {
        std::lock_guard<std::mutex> lock(mutex_);
        return func(value_);
    }

private:
    T value_;
    std::mutex mutex_;
};

// Smart pointer with cross-language reference counting
template<typename T>
class SharedPtr {
public:
    explicit SharedPtr(T* ptr) : ptr_(ptr) {}
    
    T* get() const { return ptr_.get(); }
    T& operator*() const { return *ptr_; }
    T* operator->() const { return ptr_.get(); }

private:
    std::shared_ptr<T> ptr_;
};

} // namespace cpj::stdlib