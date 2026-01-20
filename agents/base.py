from abc import ABC, abstractmethod
from typing import Any
from environments.games import GameState

class Agent(ABC):
    """
    Abstract base class for any agent in the system.
    """
    
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def get_action(self, state: GameState) -> Any:
        """
        Decide on an action given the current game state.
        """
        pass
    
    def __str__(self):
        return f"Agent({self.name})"
