from neuron import Neuron
from ket import Ket
from typing import Dict, Any
import numpy as np

class QuantumNeuron(Neuron, Ket):
    def __init__(self, **kwargs: Dict[str, Any]):
        Neuron.__init__(self, **kwargs)
        Ket.__init__(self, **kwargs)
        self.input_vector = np.append(self.state_vector, [1])  # Use state_vector from Ket and append bias term

    def feed_forward(self):
        """Override feed_forward to use the quantum state vector as input."""
        self.signal = np.tanh(np.dot(self.input_vector, self.weights.T)) + self.bias
        self.state, self.output = self.signal[0], self.signal[1]
        self.last_input = self.signal
        return [self.state, self.output]

    def iterate(self):
        """Override iterate to use quantum state vector for each iteration."""
        predictions = self.feed_forward()
        gradient, error = self.compute_gradient(predictions[1])
        self.weights -= self.learning_rate * gradient.astype(self.weights.dtype)
        self.bias -= self.learning_rate * error
        return self


if __name__ == "__main__":
    # Example usage:
    print('begin test')
    ket_instance = QuantumNeuron(label=1)
    sine_wave = QuantumNeuron.generate_noisy_sin()
    for x in range(len(sine_wave[0])):
        ket_instance.x = sine_wave[0][x]
        ket_instance.y = sine_wave[1][x]
        ket_instance.iterate()
        if x % 10 == 0:
            print(f"iteration:{x} state:{ket_instance.state} output:{ket_instance.output}")
            print('')

    print(f'prediction: {ket_instance.output} res: {ket_instance.y}')
