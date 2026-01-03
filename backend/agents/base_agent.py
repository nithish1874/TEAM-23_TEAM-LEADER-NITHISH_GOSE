"""
Base agent class
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process input and return output
        Must be implemented by subclasses
        """
        pass
    
    def validate_input(self, input_data: Dict[str, Any], required_fields: list) -> bool:
        """Validate that required fields are present"""
        for field in required_fields:
            if field not in input_data:
                raise ValueError(f"Missing required field: {field}")
        return True

