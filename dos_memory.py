"""
DOS Memory Manager - Python Implementation
"""
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class MemorySegment:
    base: int
    size: int
    used: bool
    owner: int

@dataclass
class ProcessControlBlock:
    pid: int
    name: str
    state: str
    priority: int
    segments: List[MemorySegment]
    registers: Dict[str, int]
    parent: int

class MemoryManager:
    def __init__(self):
        self.memory = bytearray(640 * 1024)  # 640K conventional memory
        self.segments = []
        self.processes = {}
        self.nextPid = 0
        self.initializeMemory()
        
    def initializeMemory(self):
        # Initially one free segment covering all memory
        self.segments.append(MemorySegment(
            base=0,
            size=len(self.memory),
            used=False,
            owner=-1
        ))
        
        # Create system process
        self.createProcess("SYSTEM", priority=0)
        
    def createProcess(self, name: str, priority: int = 1) -> int:
        """Create a new process"""
        pid = self.nextPid
        self.nextPid += 1
        
        pcb = ProcessControlBlock(
            pid=pid,
            name=name,
            state="READY",
            priority=priority,
            segments=[],
            registers={},
            parent=-1
        )
        
        self.processes[pid] = pcb
        return pid
        
    def allocateMemory(self, pid: int, size: int) -> Optional[MemorySegment]:
        """Allocate memory for a process"""
        if pid not in self.processes:
            return None
            
        # Find best fit segment
        bestFit = None
        bestSize = len(self.memory) + 1
        
        for segment in self.segments:
            if not segment.used and segment.size >= size:
                if segment.size < bestSize:
                    bestFit = segment
                    bestSize = segment.size
                    
        if bestFit is None:
            return None
            
        # Split segment if necessary
        if bestFit.size > size:
            newSegment = MemorySegment(
                base=bestFit.base + size,
                size=bestFit.size - size,
                used=False,
                owner=-1
            )
            self.segments.append(newSegment)
            bestFit.size = size
            
        bestFit.used = True
        bestFit.owner = pid
        self.processes[pid].segments.append(bestFit)
        return bestFit
        
    def freeMemory(self, pid: int):
        """Free all memory owned by a process"""
        if pid not in self.processes:
            return
            
        for segment in self.processes[pid].segments:
            segment.used = False
            segment.owner = -1
            
        self.processes[pid].segments.clear()
        self.mergeSegments()
        
    def mergeSegments(self):
        """Merge adjacent free segments"""
        i = 0
        while i < len(self.segments) - 1:
            current = self.segments[i]
            next_ = self.segments[i + 1]
            
            if not current.used and not next_.used:
                # Merge segments
                current.size += next_.size
                self.segments.pop(i + 1)
            else:
                i += 1
                
    def terminateProcess(self, pid: int) -> bool:
        """Terminate a process"""
        if pid not in self.processes or pid == 0:  # Can't terminate system process
            return False
            
        self.freeMemory(pid)
        self.processes[pid].state = "TERMINATED"
        return True
        
    def getProcessInfo(self, pid: int) -> Optional[ProcessControlBlock]:
        """Get process information"""
        return self.processes.get(pid)
        
    def listProcesses(self) -> List[ProcessControlBlock]:
        """List all processes"""
        return list(self.processes.values())
        
    def getMemoryMap(self) -> List[MemorySegment]:
        """Get memory segment map"""
        return self.segments
        
    def getMemoryUsage(self) -> Dict[str, int]:
        """Get memory usage statistics"""
        total = len(self.memory)
        used = 0
        for segment in self.segments:
            if segment.used:
                used += segment.size
                
        return {
            "total": total,
            "used": used,
            "free": total - used
        }

class MemoryCommands:
    def __init__(self, memoryManager: MemoryManager):
        self.mm = memoryManager
        
    def mem(self):
        """Display memory usage"""
        usage = self.mm.getMemoryUsage()
        print("Memory Statistics:")
        print(f"Total Memory:  {usage['total']:8,d} bytes")
        print(f"Used Memory:   {usage['used']:8,d} bytes")
        print(f"Free Memory:   {usage['free']:8,d} bytes")
        
        print("\nMemory Map:")
        for segment in self.mm.getMemoryMap():
            status = f"PID {segment.owner}" if segment.used else "Free"
            print(f"Base: {segment.base:06X}  Size: {segment.size:6,d}  Status: {status}")
            
    def tasks(self):
        """List running processes"""
        print("PID  Name                 Status    Pri   Memory")
        print("---  -------------------- --------- ---   ------")
        
        for pcb in self.mm.listProcesses():
            memUsed = sum(segment.size for segment in pcb.segments)
            print(f"{pcb.pid:3d}  {pcb.name:20s} {pcb.state:9s} {pcb.priority:3d}   {memUsed:6,d}")
            
    def kill(self, pid: int):
        """Terminate a process"""
        if self.mm.terminateProcess(pid):
            print(f"Process {pid} terminated")
        else:
            print("Invalid process ID")
