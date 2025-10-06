"""
Memory Manager Test Script
"""
from dos_memory import MemoryManager, MemoryCommands

def main():
    # Create memory manager
    mm = MemoryManager()
    commands = MemoryCommands(mm)
    
    print("Initial state:")
    commands.mem()
    print("\nInitial processes:")
    commands.tasks()
    
    # Create some test processes
    print("\nCreating test processes...")
    pid1 = mm.createProcess("TEST1", 1)
    pid2 = mm.createProcess("TEST2", 2)
    
    # Allocate memory
    print(f"\nAllocating memory for process {pid1}")
    seg1 = mm.allocateMemory(pid1, 16384)  # 16K
    print(f"Allocated {seg1.size} bytes at {hex(seg1.base)}")
    
    print(f"\nAllocating memory for process {pid2}")
    seg2 = mm.allocateMemory(pid2, 32768)  # 32K
    print(f"Allocated {seg2.size} bytes at {hex(seg2.base)}")
    
    print("\nMemory state after allocations:")
    commands.mem()
    print("\nProcess list after allocations:")
    commands.tasks()
    
    # Test process termination
    print(f"\nTerminating process {pid1}")
    commands.kill(pid1)
    
    print("\nFinal memory state:")
    commands.mem()
    print("\nFinal process list:")
    commands.tasks()

if __name__ == "__main__":
    main()