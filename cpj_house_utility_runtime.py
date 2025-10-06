"""Runtime management for utility features."""

from typing import Dict, Any, Optional, List, Callable, Set
from cpj_type_system import TypeSystem
from cpj_house_utility import (
    Table, Desk, Counter, Workbench, Cabinet,
    UtilityKind, WorkItem, WorkContext
)

class UtilityManager:
    """Manages utility features in the house"""
    
    def __init__(self, type_system: TypeSystem):
        self._type_system = type_system
        self._tables = {}
        self._desks = {}
        self._counters = {}
        self._workbenches = {}
        self._cabinets = {}
        
    def create_table(self, name: str) -> Table:
        """Create a new table for workspace organization"""
        table = Table(
            type_system=self._type_system,
            name=name
        )
        self._tables[name] = table
        return table
        
    def create_desk(self, name: str) -> Desk:
        """Create a new desk for context management"""
        desk = Desk(
            type_system=self._type_system,
            name=name
        )
        self._desks[name] = desk
        return desk
        
    def create_counter(self, name: str) -> Counter:
        """Create a new counter for pipeline processing"""
        counter = Counter(
            type_system=self._type_system,
            name=name
        )
        self._counters[name] = counter
        return counter
        
    def create_workbench(self, name: str) -> Workbench:
        """Create a new workbench for tool management"""
        workbench = Workbench(
            type_system=self._type_system,
            name=name
        )
        self._workbenches[name] = workbench
        return workbench
        
    def create_cabinet(self, name: str) -> Cabinet:
        """Create a new cabinet for resource management"""
        cabinet = Cabinet(
            type_system=self._type_system,
            name=name
        )
        self._cabinets[name] = cabinet
        return cabinet
        
    def get_table(self, name: str) -> Optional[Table]:
        """Get a table by name"""
        return self._tables.get(name)
        
    def get_desk(self, name: str) -> Optional[Desk]:
        """Get a desk by name"""
        return self._desks.get(name)
        
    def get_counter(self, name: str) -> Optional[Counter]:
        """Get a counter by name"""
        return self._counters.get(name)
        
    def get_workbench(self, name: str) -> Optional[Workbench]:
        """Get a workbench by name"""
        return self._workbenches.get(name)
        
    def get_cabinet(self, name: str) -> Optional[Cabinet]:
        """Get a cabinet by name"""
        return self._cabinets.get(name)
        
    def list_utility_features(self) -> Dict[str, List[str]]:
        """List all utility features by type"""
        return {
            'tables': list(self._tables.keys()),
            'desks': list(self._desks.keys()),
            'counters': list(self._counters.keys()),
            'workbenches': list(self._workbenches.keys()),
            'cabinets': list(self._cabinets.keys())
        }
        
    def create_work_item(self, name: str, kind: str, data: Any,
                        metadata: Optional[Dict[str, Any]] = None,
                        dependencies: Optional[Set[str]] = None,
                        tags: Optional[Set[str]] = None) -> WorkItem:
        """Create a new work item"""
        return WorkItem(
            name=name,
            kind=kind,
            data=data,
            metadata=metadata or {},
            dependencies=dependencies or set(),
            tags=tags or set()
        )
        
    def create_pipeline(self, counter_name: str, pipeline_name: str,
                       steps: List[Callable]) -> bool:
        """Create and configure a processing pipeline"""
        counter = self.get_counter(counter_name)
        if counter and counter.create_pipeline(pipeline_name):
            for step in steps:
                counter.add_step(pipeline_name, step)
            return True
        return False