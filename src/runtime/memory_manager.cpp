#include "memory_manager.h"
#include <cstdlib>
#include <iostream>

namespace cpj
{

    MemoryManager &MemoryManager::instance()
    {
        static MemoryManager mgr;
        return mgr;
    }

    void *MemoryManager::allocate(size_t size, bool managed)
    {
        std::lock_guard<std::mutex> lock(mtx);
        void *ptr = std::malloc(size);
        if (ptr)
        {
            allocations[ptr] = {ptr, size, managed};
        }
        return ptr;
    }

    void MemoryManager::deallocate(void *ptr)
    {
        std::lock_guard<std::mutex> lock(mtx);
        auto it = allocations.find(ptr);
        if (it != allocations.end())
        {
            std::free(ptr);
            allocations.erase(it);
        }
    }

    size_t MemoryManager::getAllocatedSize(void *ptr) const
    {
        std::lock_guard<std::mutex> lock(mtx);
        auto it = allocations.find(ptr);
        return (it != allocations.end()) ? it->second.size : 0;
    }

    void MemoryManager::collectGarbage()
    {
        std::lock_guard<std::mutex> lock(mtx);
        for (auto it = allocations.begin(); it != allocations.end();)
        {
            if (it->second.managed)
            {
                std::free(it->first);
                it = allocations.erase(it);
            }
            else
            {
                ++it;
            }
        }
    }

} // namespace cpj
