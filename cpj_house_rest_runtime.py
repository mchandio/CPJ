"""Runtime management for rest features."""

from typing import Dict, Any, Optional, List, Callable, Awaitable, Tuple
from cpj_type_system import TypeSystem
from cpj_house_rest import (
    Bed, Chair, Couch, Hammock, Bench,
    RestKind, AsyncTask, SuspensionState
)

class RestManager:
    """Manages rest features in the house"""
    
    def __init__(self, type_system: TypeSystem):
        self._type_system = type_system
        self._beds = {}
        self._chairs = {}
        self._couches = {}
        self._hammocks = {}
        self._benches = {}
        
    def create_bed(self, name: str, capacity: int = 10) -> Bed:
        """Create a new bed for process suspension"""
        bed = Bed(
            type_system=self._type_system,
            name=name,
            capacity=capacity
        )
        self._beds[name] = bed
        return bed
        
    def create_chair(self, name: str, max_concurrent: int = 5) -> Chair:
        """Create a new chair for async operations"""
        chair = Chair(
            type_system=self._type_system,
            name=name,
            max_concurrent=max_concurrent
        )
        self._chairs[name] = chair
        return chair
        
    def create_couch(self, name: str) -> Couch:
        """Create a new couch for cooperative multitasking"""
        couch = Couch(
            type_system=self._type_system,
            name=name
        )
        self._couches[name] = couch
        return couch
        
    def create_hammock(self, name: str) -> Hammock:
        """Create a new hammock for lazy evaluation"""
        hammock = Hammock(
            type_system=self._type_system,
            name=name
        )
        self._hammocks[name] = hammock
        return hammock
        
    def create_bench(self, name: str, workers: int = 4) -> Bench:
        """Create a new bench for parallel processing"""
        bench = Bench(
            type_system=self._type_system,
            name=name,
            workers=workers
        )
        self._benches[name] = bench
        return bench
        
    def get_bed(self, name: str) -> Optional[Bed]:
        """Get a bed by name"""
        return self._beds.get(name)
        
    def get_chair(self, name: str) -> Optional[Chair]:
        """Get a chair by name"""
        return self._chairs.get(name)
        
    def get_couch(self, name: str) -> Optional[Couch]:
        """Get a couch by name"""
        return self._couches.get(name)
        
    def get_hammock(self, name: str) -> Optional[Hammock]:
        """Get a hammock by name"""
        return self._hammocks.get(name)
        
    def get_bench(self, name: str) -> Optional[Bench]:
        """Get a bench by name"""
        return self._benches.get(name)
        
    def list_rest_features(self) -> Dict[str, List[str]]:
        """List all rest features by type"""
        return {
            'beds': list(self._beds.keys()),
            'chairs': list(self._chairs.keys()),
            'couches': list(self._couches.keys()),
            'hammocks': list(self._hammocks.keys()),
            'benches': list(self._benches.keys())
        }
        
    async def suspend_process(self, bed_name: str, process_id: str,
                            duration: Optional[float] = None,
                            context: Optional[Dict[str, Any]] = None,
                            priority: int = 0) -> bool:
        """Suspend a process in a bed"""
        bed = self.get_bed(bed_name)
        if bed:
            return await bed.suspend(process_id, duration, context, priority)
        return False
        
    async def execute_async(self, chair_name: str, task_name: str,
                          coroutine: Awaitable) -> Optional[AsyncTask]:
        """Execute an async task in a chair"""
        chair = self.get_chair(chair_name)
        if chair:
            return await chair.execute(task_name, coroutine)
        return None
        
    async def run_parallel(self, bench_name: str,
                          tasks: List[Tuple[str, Callable]]) -> Dict[str, Any]:
        """Run tasks in parallel on a bench"""
        bench = self.get_bench(bench_name)
        if bench:
            await bench.process_parallel(tasks)
            return {
                task_id: bench.get_result(task_id)
                for task_id, _ in tasks
            }
        return {}