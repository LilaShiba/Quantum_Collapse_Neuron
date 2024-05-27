from typing import Dict, Any
import numpy as np
import pandas as pd

class Ket:
    '''🔮 Quantum State Representation for One Qubit.'''
    h = 6.626 * 10**-34  # Planck's constant in J·s
    kb = 1.381 * 10**-23 # Boltzmann constant in J/K

    def __init__(self, label: int = 0, **kwargs: Dict[str, Any]):
        self.label = label
        self.state_vector = kwargs.get('state_vector', self.random_state_vector() ) # Initialize to a random state (alpha, beta) amplutudes 
        self.t = kwargs.get('t', 1)  # Kelvin, default to 1 if not provided
        
        self.c = kwargs.get('c', 0)  # Dimensionless Scaler, default to 0 if not provided
        self.k = kwargs.get('k', 0)  # surface gravity, default to 0 if not provided
        self.kbt = self.kb * self.t
        self.thermal_energy = self.kbt / self.h
        self.tl = (1 / (2 * np.pi)) * (self.h / self.kbt) if self.kbt != 0 else 0  # Avoid division by zero

        if 'csv_file' in kwargs:
            csv_file = kwargs['csv_file']
            self.load_data_from_csv(csv_file)

    def random_state_vector(self):
        '''Generate a random state vector |ψ⟩ = α|0⟩ + β|1⟩ with normalization.'''
        alpha = np.random.rand() + 1j * np.random.rand()
        beta = np.random.rand() + 1j * np.random.rand()
        norm = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2)
        alpha /= norm
        beta /= norm
        return np.array([alpha, beta], dtype=complex)

    def load_data_from_csv(self, csv_file: str, idx: int = 0):
        try:
            data = pd.read_csv(csv_file)
            alpha = data['alpha'].to_numpy(dtype=complex)
            beta = data['beta'].to_numpy(dtype=complex)
            self.state_vector = np.array([alpha[idx], beta[idx]], dtype=complex)
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def apply_hadamard(self):
        '''✨ Apply Hadamard gate to the qubit state.'''
        H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        self.state_vector = np.dot(H, self.state_vector)

    def apply_pauli_x(self):
        '''🔄 Apply Pauli-X (NOT) gate to the qubit state.'''
        X = np.array([[0, 1], [1, 0]])
        self.state_vector = np.dot(X, self.state_vector)

    def apply_pauli_y(self):
        '''💫 Apply Pauli-Y gate to the qubit state.'''
        Y = np.array([[0, -1j], [1j, 0]])
        self.state_vector = np.dot(Y, self.state_vector)

    def apply_pauli_z(self):
        '''🌀 Apply Pauli-Z gate to the qubit state.'''
        Z = np.array([[1, 0], [0, -1]])
        self.state_vector = np.dot(Z, self.state_vector)

    def measure(self) -> int:
        '''📏 Measure the qubit state in the computational basis.'''
        probabilities = np.abs(self.state_vector) ** 2
        return np.random.choice([0, 1], p=probabilities)

# Example usage:
if __name__ == "__main__":
    ket_instance = Ket(label=1, csv_file='quantum_neuron/utils/data/photon.csv')
    measurement_result = ket_instance.measure()
    print(f"Measurement result: {measurement_result}")
    ket_instance.apply_hadamard()
    measurement_result = ket_instance.measure()
    print(f"Measurement result: {measurement_result}")
    print(f"Thermal Energy Result: {ket_instance.thermal_energy}")
    print(f"Surface Gravity Lower Bound: {ket_instance.tl}")
