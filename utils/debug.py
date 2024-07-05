from neuron import Neuron
from qubit import Qubit
from bloch_sphere import BlochSphere
import numpy as np

qubit = Qubit(a=1/np.sqrt(2), b=1/np.sqrt(2))
qubit.plot_qubit()