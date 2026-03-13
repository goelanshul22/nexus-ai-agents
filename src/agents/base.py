from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    async def act(self, task_description: str, context: Dict[str, Any]) -> Any:
        pass

class SpecializedAgent(BaseAgent):
    """
    Implementation of a specialized agent capable of using specific tools.
    """
    async def act(self, task_description: str, context: Dict[str, Any]) -> str:
        print(f"[{self.name}] Acting on: {task_description}")
        # In a real scenario, this would use tools like Search, SQL, or Python interpreter
        return f"Successfully processed {task_description} using {self.role} expertise."