#pragma once

#include <cstddef>
#include <memory>
#include <mutex>
#include <unordered_map>

namespace cpj
{

    // Unified memory block for C++, Python, Java
    struct MemoryBlock
    {
        void *ptr;
        size_t size;
        bool managed;
    };

    class MemoryManager
    {
    public:
        static MemoryManager &instance();
        void *allocate(size_t size, bool managed = true);
        void deallocate(void *ptr);
        size_t getAllocatedSize(void *ptr) const;
        void collectGarbage();

    private:
        MemoryManager() = default;
        std::unordered_map<void *, MemoryBlock> allocations;
        mutable std::mutex mtx;
    };

} // namespace cpj
