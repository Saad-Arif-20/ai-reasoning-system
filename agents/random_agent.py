from agents.base import Agent
from environments.games import GameState
from typing import Any
import random

class RandomAgent(Agent):
    """
    An agent that makes completely random legal moves.
    Useful as a baseline to test against smart agents.
    """
    
    def __init__(self, name: str = "RandomBot"):
        super().__init__(name)
        
    def get_action(self, state: GameState) -> Any:
        moves = state.get_legal_moves()
        if not moves:
            return None
        return random.choice(moves)
