"""CPJ House Utility Features
Provides utility features like tables and desks for workspace and context management.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, TypeVar, Generic
from enum import Enum, auto
from cpj_type_system import TypeSystem, TypeKind, WallSection
from cpj_parser2 import Node
from cpj_enums import NodeType
from cpj_enums import AccessLevel

T = TypeVar('T')

class UtilityKind(Enum):
    """Types of utility features"""
    TABLE = auto()       # Workspace organization
    DESK = auto()        # Context management
    COUNTER = auto()     # Pipeline processing
    WORKBENCH = auto()   # Tool management
    CABINET = auto()     # Resource management

@dataclass
class WorkItem:
    """Individual work item in a workspace"""
    name: str
    kind: str
    data: Any
    metadata: Dict[str, Any] = field(default_factory=dict)
    dependencies: Set[str] = field(default_factory=set)
    tags: Set[str] = field(default_factory=set)

@dataclass
class WorkContext:
    """Execution context information"""
    name: str
    variables: Dict[str, Any]
    parent: Optional['WorkContext'] = None
    children: List['WorkContext'] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Table(Node):
    """Workspace organization"""
    name: str = field(default="")
    kind: UtilityKind = field(default=UtilityKind.TABLE)
    _workspaces: Dict[str, Dict[str, WorkItem]] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.UTILITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def create_workspace(self, name: str) -> bool:
        """Create a new workspace"""
        if name in self._workspaces:
            return False
        self._workspaces[name] = {}
        return True
        
    def add_work_item(self, workspace: str, item: WorkItem) -> bool:
        """Add a work item to a workspace"""
        if workspace not in self._workspaces:
            return False
            
        self._workspaces[workspace][item.name] = item
        return True
        
    def get_work_item(self, workspace: str, name: str) -> Optional[WorkItem]:
        """Get a work item from a workspace"""
        return self._workspaces.get(workspace, {}).get(name)
        
    def list_workspaces(self) -> List[str]:
        """List all workspaces"""
        return list(self._workspaces.keys())
        
    def list_work_items(self, workspace: str) -> List[str]:
        """List all work items in a workspace"""
        return list(self._workspaces.get(workspace, {}).keys())
        
    def find_by_tag(self, workspace: str, tag: str) -> List[WorkItem]:
        """Find work items by tag"""
        items = self._workspaces.get(workspace, {})
        return [item for item in items.values() if tag in item.tags]

@dataclass
class Desk(Node):
    """Context management"""
    name: str = field(default="")
    kind: UtilityKind = field(default=UtilityKind.DESK)
    _contexts: Dict[str, WorkContext] = field(default_factory=dict)
    _active_context: Optional[str] = None
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.UTILITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def create_context(self, name: str, parent: Optional[str] = None) -> WorkContext:
        """Create a new context"""
        context = WorkContext(
            name=name,
            variables={},
            parent=self._contexts.get(parent) if parent else None
        )
        self._contexts[name] = context
        if parent and parent in self._contexts:
            self._contexts[parent].children.append(context)
        return context
        
    def set_active_context(self, name: str) -> bool:
        """Set the active context"""
        if name in self._contexts:
            self._active_context = name
            return True
        return False
        
    def get_context(self, name: str) -> Optional[WorkContext]:
        """Get a context by name"""
        return self._contexts.get(name)
        
    def get_active_context(self) -> Optional[WorkContext]:
        """Get the currently active context"""
        return self._contexts.get(self._active_context) if self._active_context else None
        
    def set_variable(self, name: str, value: Any, context_name: Optional[str] = None) -> bool:
        """Set a variable in a context"""
        context = (self._contexts.get(context_name) if context_name 
                  else self.get_active_context())
        if context:
            context.variables[name] = value
            return True
        return False
        
    def get_variable(self, name: str, context_name: Optional[str] = None) -> Optional[Any]:
        """Get a variable from a context"""
        context = (self._contexts.get(context_name) if context_name 
                  else self.get_active_context())
        if not context:
            return None
            
        # Search current context and parents
        while context:
            if name in context.variables:
                return context.variables[name]
            context = context.parent
            
        return None

@dataclass
class Counter(Node):
    """Pipeline processing support"""
    name: str = field(default="")
    kind: UtilityKind = field(default=UtilityKind.COUNTER)
    _pipelines: Dict[str, List[Callable]] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.UTILITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def create_pipeline(self, name: str) -> bool:
        """Create a new processing pipeline"""
        if name in self._pipelines:
            return False
        self._pipelines[name] = []
        return True
        
    def add_step(self, pipeline: str, step: Callable) -> bool:
        """Add a processing step to a pipeline"""
        if pipeline not in self._pipelines:
            return False
        self._pipelines[pipeline].append(step)
        return True
        
    def process(self, pipeline: str, input_data: Any) -> Any:
        """Process data through a pipeline"""
        if pipeline not in self._pipelines:
            return input_data
            
        result = input_data
        for step in self._pipelines[pipeline]:
            result = step(result)
        return result

@dataclass
class Workbench(Node):
    """Tool management"""
    name: str = field(default="")
    kind: UtilityKind = field(default=UtilityKind.WORKBENCH)
    _tools: Dict[str, Callable] = field(default_factory=dict)
    _tool_metadata: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.UTILITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def register_tool(self, name: str, tool: Callable, metadata: Optional[Dict[str, Any]] = None):
        """Register a new tool"""
        self._tools[name] = tool
        if metadata:
            self._tool_metadata[name] = metadata
            
    def use_tool(self, name: str, *args, **kwargs) -> Any:
        """Use a registered tool"""
        tool = self._tools.get(name)
        if tool:
            return tool(*args, **kwargs)
        raise ValueError(f"Tool not found: {name}")
        
    def get_tool_info(self, name: str) -> Optional[Dict[str, Any]]:
        """Get tool metadata"""
        return self._tool_metadata.get(name)
        
    def list_tools(self) -> List[str]:
        """List all registered tools"""
        return list(self._tools.keys())

@dataclass
class Cabinet(Node):
    """Resource management"""
    name: str = field(default="")
    kind: UtilityKind = field(default=UtilityKind.CABINET)
    _resources: Dict[str, Any] = field(default_factory=dict)
    _resource_refs: Dict[str, int] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.UTILITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_resource(self, name: str, resource: Any) -> bool:
        """Add a new resource"""
        if name in self._resources:
            return False
        self._resources[name] = resource
        self._resource_refs[name] = 0
        return True
        
    def acquire(self, name: str) -> Optional[Any]:
        """Acquire a resource (increment reference count)"""
        if name in self._resources:
            self._resource_refs[name] += 1
            return self._resources[name]
        return None
        
    def release(self, name: str) -> bool:
        """Release a resource (decrement reference count)"""
        if name in self._resource_refs and self._resource_refs[name] > 0:
            self._resource_refs[name] -= 1
            return True
        return False
        
    def get_ref_count(self, name: str) -> int:
        """Get current reference count for a resource"""
        return self._resource_refs.get(name, 0)