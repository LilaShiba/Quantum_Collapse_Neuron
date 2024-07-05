import numpy as np
from typing import Dict
from bloch_sphere import BlochSphere
import matplotlib.pyplot as plt

class Qubit(BlochSphere):
    """
    Class representing a qubit, inheriting from BlochSphere.

    Provides methods for setting the qubit state and visualizing it on the Bloch sphere.
    """

    def __init__(self, **kwargs: Dict[str, complex]) -> None:
        """
        Initialize the qubit with given state coefficients.

        :param kwargs: Dictionary containing 'a' and 'b' as complex coefficients.
        """
        super().__init__()
        self.a = kwargs.get('a', 1 + 0j)  # Default a to 1 if not provided
        self.b = kwargs.get('b', 0 + 0j)  # Default b to 0 if not provided
        self.normalize()

    def normalize(self) -> None:
        """Normalize the qubit state to ensure |a|^2 + |b|^2 = 1."""
        norm = np.sqrt(abs(self.a)**2 + abs(self.b)**2)
        self.a /= norm
        self.b /= norm

    def plot_qubit(self) -> None:
        """
        Plot the qubit state on the Bloch sphere.

        The qubit state is represented by the angles θ and φ.
        """
        # Calculate θ and φ from the state coefficients
        theta = 2 * np.arctan2(abs(self.b), abs(self.a))
        phi = np.angle(self.b) - np.angle(self.a)

        # Calculate the Cartesian coordinates
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)

        # Plot the Bloch sphere
        self.plot_sphere()

        # Plot the qubit state
        self.ax.quiver(0, 0, 0, x, y, z, color='k', arrow_length_ratio=0.1)
        self.ax.text(x, y, z, r'$|\psi\rangle$', color='k')

        # Show the plot
        plt.show()
