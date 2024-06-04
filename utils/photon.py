import numpy as np
from typing import Dict, Any

class Photon():
    '''
    Encoded photon via quantum state
    '''

    def __init__(self, **kwargs: Dict[str, Any]):
        self.label: str = kwargs.get('label', '')
        self.alpha: float
        self.beta: float
        self.polarization: float 
        self.spin: float 
        self.current_instance: list 
        self.output: list 
        self.input: list 
        self.state: float
        self.state_space: list