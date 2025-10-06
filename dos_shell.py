from dataclasses import dataclass
from typing import List, Dict, Optional

"""
CPJ-DOS: A DOS-like operating system implementation in CPJ
Demonstrates multi-language integration and low-level system access
"""

from dos_memory import MemoryManager, MemoryCommands

# Core OS definitions
@dataclass
class MemoryBlock :
    address: int
    size: int
    allocated: bool


    @dataclass
    class FileDescriptor :
        name: str
        size: int
        attributes: int
        cluster: int


        @dataclass
        class ProcessInfo :
            pid: int
            name: str
            memory: int
            status: str


            # System configuration
            MEMORY_SIZE = 640 * 1024  # 640K ought to be enough for anybody ;)
            MAX_FILES = 256
            MAX_PROCESSES = 64

            # DOS Shell implementation
            class DOSShell :
                # private:
                    currentDir: str
                    fileTable: List[FileDescriptor]
                    running: bool
                    memoryManager: MemoryManager
                    memoryCommands: MemoryCommands

                    # public:
                        def __init__(self) :
                            self.currentDir = "C:\\"
                            self.fileTable = []
                            self.running = true
                            self.memoryManager = MemoryManager()
                            self.memoryCommands = MemoryCommands(self.memoryManager)
                            self.initializeSystem()


                            def initializeSystem(self)  :
                                # Set up root directory
                                self.fileTable.append(FileDescriptor(
                                name="C:",
                                size=0,
                                attributes=0x10,  # Directory attribute
                                cluster=0
                                ))


                                def run(self)  :
                                    print("CPJ-DOS version 1.0")
                                    print("Copyright (C) 2025 CPJ Development Team")
                                    print("")

                                    while self.running :
                                        try :
                                            print(f":self.currentDir>", end="")
                                            command = input().strip()
                                            self.executeCommand(command)
                                        except Exception as e :
                                            print(f"Error: :str(e)")




                                            def executeCommand(self, command: str)  :
                                                # Split command and arguments
                                                parts = command.split()
                                                if len(parts) == 0:
                                                    return

                                                    cmd = parts[0].upper()
                                                    args = parts[1:]

                                                    match cmd :
                                                        case "DIR":
                                                            self.commandDir(args)
                                                            case "CD":
                                                                self.commandCd(args)
                                                                case "COPY":
                                                                    self.commandCopy(args)
                                                                    case "DEL":
                                                                        self.commandDel(args)
                                                                        case "EXIT":
                                                                            self.running = false
                                                                            case "HELP":
                                                                                self.commandHelp(args)
                                                                                case "MEM":
                                                                                    self.memoryCommands.mem()
                                                                                    case "TASKS":
                                                                                        self.memoryCommands.tasks()
                                                                                        case "KILL":
                                                                                            if len(args) > 0:
                                                                                                try:
                                                                                                    pid = int(args[0])
                                                                                                    self.memoryCommands.kill(pid)
                                                                                                except ValueError:
                                                                                                    print("Invalid process ID")
                                                                                                else:
                                                                                                    print("KILL requires a process ID")
                                                                                                    case "TYPE":
                                                                                                        self.commandType(args)
                                                                                                        case _:
                                                                                                            if command.endswith(".COM") or command.endswith(".EXE"):
                                                                                                                self.executeProgram(command)
                                                                                                            else:
                                                                                                                print("Bad command or file name")



                                                                                                                # Command implementations
                                                                                                                def commandDir(self, args: List[str])  :
                                                                                                                    print(" Directory of " + self.currentDir)
                                                                                                                    print("")
                                                                                                                    totalFiles = 0
                                                                                                                    totalBytes = 0

                                                                                                                    for file in self.fileTable :
                                                                                                                        if self.isInCurrentDir(file) :
                                                                                                                            attr = "<DIR>" if file.attributes & 0x10 else "     "
                                                                                                                            print(f":file.name:8 :attr :file.size:8,d")
                                                                                                                            totalFiles += 1
                                                                                                                            totalBytes += file.size



                                                                                                                            print(f":totalFiles File(s) :totalBytes:,d bytes")
                                                                                                                            print(f":self.getFreeSpace():,d bytes free")


                                                                                                                            def commandCd(self, args: List[str])  :
                                                                                                                                if len(args) == 0 :
                                                                                                                                    print(self.currentDir)
                                                                                                                                    return


                                                                                                                                    newDir = args[0]
                                                                                                                                    if newDir == ".." :
                                                                                                                                        if self.currentDir != "C:\\":
                                                                                                                                            self.currentDir = "\\".join(self.currentDir.split("\\")[:-1])
                                                                                                                                            if not self.currentDir.endswith("\\"):
                                                                                                                                                self.currentDir += "\\"
                                                                                                                                                else :
                                                                                                                                                    if self.directoryExists(newDir):
                                                                                                                                                        if not newDir.endswith("\\"):
                                                                                                                                                            newDir += "\\"
                                                                                                                                                            self.currentDir = f"C::newDir" if not newDir.startswith("\\") else f"C::newDir"
                                                                                                                                                        else:
                                                                                                                                                            print("Invalid directory")



                                                                                                                                                            # Utility methods
                                                                                                                                                            def isInCurrentDir(self, file: FileDescriptor) -> bool :
                                                                                                                                                                # Check if file is in current directory
                                                                                                                                                                filePath = file.name.split("\\")
                                                                                                                                                                currentPath = self.currentDir[2:].split("\\") # Remove C:
                                                                                                                                                                    return filePath[:-1] == currentPath[:-1]


                                                                                                                                                                    def directoryExists(self, dir: str) -> bool :
                                                                                                                                                                        for file in self.fileTable :
                                                                                                                                                                            if file.attributes & 0x10 and file.name == dir:
                                                                                                                                                                                return true

                                                                                                                                                                                return false


                                                                                                                                                                                def getFreeSpace(self) -> int :
                                                                                                                                                                                    used = 0
                                                                                                                                                                                    for block in self.memoryMap :
                                                                                                                                                                                        if block.allocated:
                                                                                                                                                                                            used += block.size

                                                                                                                                                                                            return MEMORY_SIZE - used


                                                                                                                                                                                            def executeProgram(self, program: str)  :
                                                                                                                                                                                                print(f"Executing :program...")
                                                                                                                                                                                                # Allocate memory
                                                                                                                                                                                                neededMemory = 64 * 1024  # Default 64K for programs
                                                                                                                                                                                                if let block = self.allocateMemory(neededMemory) :
                                                                                                                                                                                                    pid = len(self.processes)
                                                                                                                                                                                                    self.processes.append(ProcessInfo(
                                                                                                                                                                                                    pid=pid,
                                                                                                                                                                                                    name=program,
                                                                                                                                                                                                    memory=neededMemory,
                                                                                                                                                                                                    status="RUNNING"
                                                                                                                                                                                                    ))
                                                                                                                                                                                                    print(f"Started process :pid")
                                                                                                                                                                                                    else :
                                                                                                                                                                                                        print("Insufficient memory")



                                                                                                                                                                                                        def allocateMemory(self, size: int) -> Optional[MemoryBlock] :
                                                                                                                                                                                                            for block in self.memoryMap :
                                                                                                                                                                                                                if not block.allocated and block.size >= size :
                                                                                                                                                                                                                    if block.size == size :
                                                                                                                                                                                                                        block.allocated = true
                                                                                                                                                                                                                        return block
                                                                                                                                                                                                                        else :
                                                                                                                                                                                                                            # Split block
                                                                                                                                                                                                                            newBlock = MemoryBlock(
                                                                                                                                                                                                                            address=block.address + size,
                                                                                                                                                                                                                            size=block.size - size,
                                                                                                                                                                                                                            allocated=false
                                                                                                                                                                                                                            )
                                                                                                                                                                                                                            block.size = size
                                                                                                                                                                                                                            block.allocated = true
                                                                                                                                                                                                                            self.memoryMap.append(newBlock)
                                                                                                                                                                                                                            return block



                                                                                                                                                                                                                            return None



                                                                                                                                                                                                                            # Main entry point
                                                                                                                                                                                                                            def main(self)  :
                                                                                                                                                                                                                                shell = DOSShell()
                                                                                                                                                                                                                                shell.run()


                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                    main()