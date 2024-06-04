import numpy as np
import matplotlib.pyplot as plt

class BlochSphere:
    """
    Class representing the Bloch sphere.

    Provides methods for visualizing the Bloch sphere.
    """

    def __init__(self) -> None:
        """Initialize the Bloch sphere."""
        pass

    def plot_sphere(self) -> None:
        """Plot the Bloch sphere with coordinate axes."""
        # Create a sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        # Create the figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the surface
        ax.plot_surface(x, y, z, color='c', alpha=0.1)

        # Plot the axes
        ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

        # Labels for axes
        ax.text(1.1, 0, 0, r'$x$', color='r')
        ax.text(0, 1.1, 0, r'$y$', color='g')
        ax.text(0, 0, 1.1, r'$z$', color='b')

        # Set the limits
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])

        self.ax = ax
