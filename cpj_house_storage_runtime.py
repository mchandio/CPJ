from typing import Dict, Any, Optional
from cpj_type_system import TypeSystem
from cpj_house_storage import (
    Cupboard, Bin, Shelf, Drawer, Chest,
    StoragePolicy, StorageKind
)

class StorageManager:
    """Manages storage features in the house"""
    
    def __init__(self, type_system: TypeSystem):
        self._type_system = type_system
        self._storage_features = {}
        
    def create_cupboard(self, name: str, policy: Optional[StoragePolicy] = None) -> Cupboard:
        """Create a new cupboard for long-term storage"""
        cupboard = Cupboard(
            type_system=self._type_system,
            name=name,
            kind=StorageKind.CUPBOARD,
            policy=policy or StoragePolicy()
        )
        self._storage_features[name] = cupboard
        return cupboard
        
    def create_bin(self, name: str, policy: Optional[StoragePolicy] = None) -> Bin:
        """Create a new bin for temporary storage"""
        bin = Bin(
            type_system=self._type_system,
            name=name,
            policy=policy or StoragePolicy(persistence=False, overflow_policy="evict")
        )
        self._storage_features[name] = bin
        return bin
        
    def create_shelf(self, name: str, policy: Optional[StoragePolicy] = None) -> Shelf:
        """Create a new shelf for ordered collections"""
        shelf = Shelf(
            type_system=self._type_system,
            name=name,
            policy=policy or StoragePolicy()
        )
        self._storage_features[name] = shelf
        return shelf
        
    def create_drawer(self, name: str, policy: Optional[StoragePolicy] = None) -> Drawer:
        """Create a new drawer for key-value storage"""
        drawer = Drawer(
            type_system=self._type_system,
            name=name,
            policy=policy or StoragePolicy()
        )
        self._storage_features[name] = drawer
        return drawer
        
    def create_chest(self, name: str, storage_path: str, policy: Optional[StoragePolicy] = None) -> Chest:
        """Create a new chest for persistent storage"""
        chest = Chest(
            type_system=self._type_system,
            name=name,
            storage_path=storage_path,
            policy=policy or StoragePolicy(persistence=True)
        )
        self._storage_features[name] = chest
        return chest
        
    def get_storage(self, name: str) -> Optional[Any]:
        """Get a storage feature by name"""
        return self._storage_features.get(name)
        
    def list_storage(self) -> Dict[str, StorageKind]:
        """List all storage features and their types"""
        return {name: storage.kind for name, storage in self._storage_features.items()}
        
    def remove_storage(self, name: str) -> bool:
        """Remove a storage feature"""
        if name in self._storage_features:
            # Ensure persistent storage is saved if needed
            storage = self._storage_features[name]
            if isinstance(storage, Chest):
                storage._save_persistent_data()
            del self._storage_features[name]
            return True
        return False