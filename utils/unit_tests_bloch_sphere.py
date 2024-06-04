import unittest
import numpy as np
from bloch_sphere import BlochSphere
from qubit import Qubit

class TestBlochSphere(unittest.TestCase):
    def test_plot_sphere(self):
        """Test if the plot_sphere method runs without errors."""
        sphere = BlochSphere()
        try:
            sphere.plot_sphere()
            result = True
        except Exception as e:
            result = False
        self.assertTrue(result, "plot_sphere method should run without errors.")

class TestQubit(unittest.TestCase):
    def test_initialization(self):
        """Test initialization of Qubit class with given coefficients."""
        qubit = Qubit(a=1/np.sqrt(2), b=1/np.sqrt(2))
        self.assertAlmostEqual(abs(qubit.a)**2 + abs(qubit.b)**2, 1.0, places=6, msg="Qubit should be normalized.")
    
    def test_default_initialization(self):
        """Test default initialization of Qubit class."""
        qubit = Qubit()
        self.assertEqual(qubit.a, 1+0j, "Default coefficient a should be 1+0j.")
        self.assertEqual(qubit.b, 0+0j, "Default coefficient b should be 0+0j.")
        self.assertAlmostEqual(abs(qubit.a)**2 + abs(qubit.b)**2, 1.0, places=6, msg="Qubit should be normalized.")
    
    def test_plot_qubit(self):
        """Test if the plot_qubit method runs without errors."""
        qubit = Qubit(a=1/np.sqrt(2), b=1/np.sqrt(2))
        try:
            qubit.plot_qubit()
            result = True
        except Exception as e:
            result = False
        self.assertTrue(result, "plot_qubit method should run without errors.")

if __name__ == "__main__":
    unittest.main()
