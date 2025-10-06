"""CPJ Roof Inspector System

Provides monitoring and diagnostic tools to check roof integrity and house protection status.
Includes automated inspection schedules and detailed reporting.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Callable
from datetime import datetime, timedelta
import threading
import logging
import json
from pathlib import Path

from cpj_roof import (RoofDamage, RoofSeverity, RoofMaterial, 
                     RoofTile, RoofSection)
from cpj_roof_guard import RoofException, map_damage_to_exception
from cpj_roof_recovery import RoofRecoveryManager

@dataclass
class InspectionResult:
    """Results from a roof inspection"""
    timestamp: datetime
    damages: List[RoofDamage]
    recovered: List[RoofDamage]
    section_status: Dict[str, bool]
    metrics: Dict[str, Any]

@dataclass
class InspectionSchedule:
    """Schedule for automated inspections"""
    interval: timedelta
    last_run: Optional[datetime] = None
    enabled: bool = True

class RoofInspector:
    """Main inspection system for the roof"""
    def __init__(self, sections: List[RoofSection], recovery_manager: RoofRecoveryManager):
        self.sections = sections
        self.recovery_manager = recovery_manager
        self.logger = logging.getLogger('cpj.roof.inspector')
        self.inspection_history: List[InspectionResult] = []
        self.schedule = InspectionSchedule(interval=timedelta(minutes=5))
        self._inspection_thread = None
        self._stop_requested = False
        
    def inspect_section(self, section: RoofSection) -> List[RoofDamage]:
        """Inspect a single roof section"""
        self.logger.debug(f"Inspecting section: {section.name}")
        return section.inspect_all()
    
    def inspect_all(self) -> InspectionResult:
        """Perform a full roof inspection"""
        damages = []
        recovered = []
        section_status = {}
        metrics = {
            'memory_usage_mb': 0,
            'open_resources': 0,
            'type_violations': 0,
            'runtime_errors': 0
        }
        
        # Inspect each section
        for section in self.sections:
            section_damages = self.inspect_section(section)
            damages.extend(section_damages)
            section_status[section.name] = not bool(section_damages)
            
            # Try recovery for each damage
            for damage in section_damages:
                if self.recovery_manager.attempt_recovery(damage):
                    recovered.append(damage)
                    damages.remove(damage)
                
                # Update metrics
                if damage.material == RoofMaterial.MEMORY:
                    metrics['memory_usage_mb'] = damage.context.get('current_mem', 0)
                elif damage.material == RoofMaterial.RESOURCE:
                    metrics['open_resources'] += len(damage.context.get('resources', []))
                elif damage.material == RoofMaterial.TYPE:
                    metrics['type_violations'] += 1
                elif damage.material == RoofMaterial.RUNTIME:
                    metrics['runtime_errors'] += 1
        
        result = InspectionResult(
            timestamp=datetime.now(),
            damages=damages,
            recovered=recovered,
            section_status=section_status,
            metrics=metrics
        )
        
        self.inspection_history.append(result)
        return result
    
    def start_automated_inspection(self):
        """Start automated inspection thread"""
        if self._inspection_thread is None:
            self._stop_requested = False
            self._inspection_thread = threading.Thread(target=self._inspection_loop)
            self._inspection_thread.daemon = True
            self._inspection_thread.start()
    
    def stop_automated_inspection(self):
        """Stop automated inspection thread"""
        if self._inspection_thread is not None:
            self._stop_requested = True
            self._inspection_thread.join()
            self._inspection_thread = None
    
    def _inspection_loop(self):
        """Background thread for automated inspections"""
        while not self._stop_requested:
            if self.schedule.enabled:
                now = datetime.now()
                if (self.schedule.last_run is None or 
                    now - self.schedule.last_run >= self.schedule.interval):
                    self.inspect_all()
                    self.schedule.last_run = now
            
            # Sleep for a short time to prevent busy waiting
            import time
            time.sleep(1)
    
    def generate_report(self, detailed: bool = False) -> Dict[str, Any]:
        """Generate inspection report"""
        if not self.inspection_history:
            return {}
            
        latest = self.inspection_history[-1]
        report = {
            'timestamp': latest.timestamp.isoformat(),
            'status': 'healthy' if not latest.damages else 'issues_detected',
            'sections': latest.section_status,
            'metrics': latest.metrics,
            'active_damages': len(latest.damages),
            'recovered_issues': len(latest.recovered)
        }
        
        if detailed:
            report['damage_details'] = [
                {
                    'severity': d.severity.name,
                    'material': d.material.name,
                    'message': d.message,
                    'context': d.context
                }
                for d in latest.damages
            ]
            report['recovery_details'] = [
                {
                    'severity': d.severity.name,
                    'material': d.material.name,
                    'message': d.message
                }
                for d in latest.recovered
            ]
            
            # Add historical trends
            report['trends'] = {
                'memory_usage': [r.metrics['memory_usage_mb'] 
                               for r in self.inspection_history[-10:]],
                'type_violations': [r.metrics['type_violations']
                                  for r in self.inspection_history[-10:]],
                'runtime_errors': [r.metrics['runtime_errors']
                                 for r in self.inspection_history[-10:]]
            }
        
        return report
    
    def save_report(self, path: Path, detailed: bool = True):
        """Save inspection report to file"""
        report = self.generate_report(detailed=detailed)
        with open(path, 'w') as f:
            json.dump(report, f, indent=2)
    
    def get_section_health(self, section_name: str) -> float:
        """Get health score for a section (0-1)"""
        if not self.inspection_history:
            return 1.0
            
        # Check last 10 inspections
        recent = self.inspection_history[-10:]
        section_results = [r.section_status.get(section_name, False) 
                         for r in recent]
        return sum(section_results) / len(section_results)
    
    def get_overall_health(self) -> float:
        """Get overall roof health score (0-1)"""
        if not self.sections or not self.inspection_history:
            return 1.0
            
        return sum(self.get_section_health(s.name) 
                  for s in self.sections) / len(self.sections)