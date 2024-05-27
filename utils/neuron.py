import numpy as np
from typing import Dict, Any
import matplotlib.pyplot as plt

class Neuron():
    def __init__(self, **kwargs: Dict[str, Any]):
        self.layer: int = kwargs.get('layer', 0)
        self.label: str = kwargs.get('label', '')
        self.x: float = kwargs.get('inputs', [0.0, 0.0])[0]
        self.y: float = kwargs.get('inputs', [0.0, 0.0])[1]
        self.weights: np.array = kwargs.get('weights', np.random.rand(2, 3))
        self.bias: float = kwargs.get('bias', np.random.random())
        self.learning_rate: float = kwargs.get('learning_rate', np.random.random())
        self.state: float = kwargs.get('state', np.random.random())
        self.output: float = kwargs.get('output', np.random.random())
        self.loss_gradient: np.array = kwargs.get('loss_gradient', None)
        self.last_input: np.array = kwargs.get('last_input', None)
        self.signal: np.array = kwargs.get('signal', None)

    def compute_gradient(self, output):
        '''distance between predictions and ground truth'''
        error = output - self.y
        derivative = 1 - np.tanh(output) ** 2
        gradient = error * derivative * self.x
        return gradient, error

    def feed_forward(self, input_vector=None) -> np.ndarray:
        """Compute the neuron's output using a simple linear activation.

        Args:
            inputs (np.ndarray): The inputs to the neuron.
            where I = 3x2 matrix. cols: (input, output), rows: examples

        Returns:
            np.ndarray: The output of the neuron after applying the weights, bias, and activation function.
        """
        if input_vector is None:
            input_vector = [self.x, self.state, 1]
        # Calculate the signal using weights and input vector
        self.signal = np.tanh(np.dot(input_vector, self.weights.T)) + self.bias
        self.state, self.output = self.signal[0], self.signal[1]
        self.last_input = self.signal
        return [self.state, self.output]

    def derivative(self):
        '''returns the derivative of the activation function'''
        return (1.0 - np.tanh(self.signal) ** 2)

    def iterate(self):
        """Compute the gradient of the neuron's weights with respect to the loss."""
        predictions = self.feed_forward()
        gradient, error = self.compute_gradient(predictions[1])
        self.weights -= self.learning_rate * gradient
        self.bias -= self.learning_rate * error
        return self

    @staticmethod
    def sigmoid(x):
        """The Sigmoid function."""
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        """Derivative of the Sigmoid function."""
        return Neuron.sigmoid(x) * (1 - Neuron.sigmoid(x))

    @staticmethod
    def generate_noisy_sin(length=100, noise_level=0.1):
        t = np.linspace(0, 2 * np.pi, length)
        sine_wave = np.sin(t)
        noise = np.random.normal(0, noise_level, sine_wave.shape)
        noisy_sine_wave = sine_wave + noise
        return np.array([t, noisy_sine_wave])


if __name__ == "__main__":
    # Example usage:
    print('begin test')
    sine_wave = Neuron.generate_noisy_sin()
    one_point = np.array([sine_wave[0][0], sine_wave[1][0]])
    neuron = Neuron(inputs=one_point, layer=1)
    
    for x in range(len(sine_wave[0])):
        neuron.x = sine_wave[0][x]
        neuron.y = sine_wave[1][x]
        neuron.iterate()
        if x % 10 == 0:
            print(f"iteration:{x} state:{neuron.state} output:{neuron.output}")
            print('')

    print(f'prediction: {neuron.output} res: {neuron.y}')
