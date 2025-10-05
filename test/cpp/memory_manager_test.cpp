#include "test_framework.h"
#include "../../src/runtime/memory_manager.h"

using namespace cpj::test;

TEST_CASE(MemoryManagerBasics) {
    auto& mm = cpj::MemoryManager::instance();
    
    // Test allocation
    void* ptr = mm.allocate(100);
    EXPECT_TRUE(ptr != nullptr);
    EXPECT_EQUAL(100UL, mm.getAllocatedSize(ptr));
    
    // Test deallocation
    mm.deallocate(ptr);
    EXPECT_EQUAL(0UL, mm.getAllocatedSize(ptr));
}

TEST_CASE(MemoryManagerGC) {
    auto& mm = cpj::MemoryManager::instance();
    
    // Allocate some managed memory
    void* ptr1 = mm.allocate(50, true);
    void* ptr2 = mm.allocate(75, true);
    
    EXPECT_TRUE(ptr1 != nullptr);
    EXPECT_TRUE(ptr2 != nullptr);
    
    // Run garbage collection
    mm.collectGarbage();
    
    // Verify memory was freed
    EXPECT_EQUAL(0UL, mm.getAllocatedSize(ptr1));
    EXPECT_EQUAL(0UL, mm.getAllocatedSize(ptr2));
}

int main() {
    auto results = TestRunner::instance().runAll();
    
    int failed = 0;
    for (const auto& result : results) {
        std::cout << result.test_name << ": " 
                 << (result.passed ? "PASSED" : "FAILED")
                 << " (" << result.duration.count() << "µs)";
        if (!result.passed) {
            std::cout << "\n  " << result.message;
            failed++;
        }
        std::cout << std::endl;
    }
    
    return failed;
}