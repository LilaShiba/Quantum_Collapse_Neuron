import numpy as np
from typing import Dict, Any, Tuple, List

class Cell():
    '''
    A 3D representation of a human-synth neuron
    prototype 1 | 2024-08-07
    '''

    def __init__(self, **kwargs: Dict[str, Any]):
        self.layer: int = kwargs.get('layer', 0)
        self.label: str = kwargs.get('label', '')
        self.dims_of_alpha: Tuple[int, int] = kwargs.get('dims_alpha', (2, 2))
        self.dims_of_beta: Tuple[int, int] = kwargs.get('dims_beta', (2, 2))

        # Will hold input data | I of I/O
        self.alpha: List[float] = kwargs.get('inputs_alpha', [0.0, 0.0])
        self.beta: List[float] = kwargs.get('inputs_beta', [0.0, 0.0])
        
        # Ensure Compatibility 
        self.entangle: np.ndarray = kwargs.get('weights', self._entangle_probs(self.alpha, self.beta))

        # Neural Net Settings (each cell diverse)
        self.bias: float = kwargs.get('bias', np.random.random())
        self.learning_rate: float = kwargs.get('learning_rate', np.random.random())
        
        # Value (think dot product or collapsed state to 1D)
        self.state: float = kwargs.get('state', np.random.random())
        self.output: float = kwargs.get('output', np.dot(self.alpha, self.beta))
        self.loss_gradient: np.ndarray = kwargs.get('loss_gradient', None)
        self.last_input: np.ndarray = kwargs.get('last_input', None)
        
        # x, y, z
        self.pos: np.ndarray = np.array(kwargs.get('pos', [0, 0, 0]))
        self.mag: float = kwargs.get('mag', 0)
        
        # orientation radians
        self.psi, self.theta = self.get_orientation()
        self.x, self.y, self.z = self.get_cartesian_coords()
        self.pos = np.array([self.x, self.y, self.z])
        self.prob_dist_matrix = self.get_prob_distro()

        # connections
        self.k: np.ndarray = kwargs.get('k', np.array([None]))

    def get_orientation(self) -> Tuple[float, float]:
        '''
        Calculates direction from 1x3 vector pos
        '''
        x, y, z = self.pos
        r = np.sqrt(x**2 + y**2 + z**2)
        
        psi = np.arctan2(y, x)  # azimuth angle
        theta = np.arccos(z / r)  # polar angle
        return psi, theta

    def _entangle_probs(self, alpha: List[float], beta: List[float]) -> np.ndarray:
        """
        Entangles two lists of probabilities to create a probability distribution matrix.

        Parameters: Independent Events
        alpha (List[float]): List of probabilities for alpha.
        beta (List[float]): List of probabilities for beta.

        Returns:
        np.ndarray: A probability distribution matrix formed by the outer product of alpha and beta.
        """
        alpha = np.array(alpha)
        beta = np.array(beta)
        entangled_matrix = np.outer(alpha, beta)  # Outer product to create the matrix
        entangled_matrix /= np.sum(entangled_matrix)  # Normalize the matrix to make it a probability distribution
        return entangled_matrix

    def get_prob_distro(self) -> np.ndarray:
        '''
        Creates a normalized probability distribution matrix
        from alpha and beta probabilities.
        u⊗v A = ui * vi
        '''
        prob_dist_matrix = self._entangle_probs(self.alpha, self.beta)
        return prob_dist_matrix
    
    def get_cartesian_coords(self) -> Tuple[float, float, float]:
        # Compute Cartesian coordinates
        x = np.sin(self.theta) * np.cos(self.psi)
        y = np.sin(self.theta) * np.sin(self.psi)
        z = np.cos(self.theta)
        return x, y, z
    



# Example usage
alpha_probs = np.random.rand(8,8)
beta_probs = np.random.rand(8,2)

cell = Cell(inputs_alpha=alpha_probs, inputs_beta=beta_probs, pos=[1.2, 2.3, 1.0])
cell.get_cartesian_coords()
print("Orientation (psi, theta):", cell.get_orientation())
print("Cartesian Coordinates (x, y, z):", cell.get_cartesian_coords())
