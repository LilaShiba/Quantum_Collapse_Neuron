<link rel="stylesheet" type="text/css" href="styles.css">

# 🧙‍♀️✨ Understanding Qubits and Measurement in Quantum Computing 🚀🌌

## What is a Qubit? 🧩

A qubit is the basic unit of quantum information, just like a bit in classical computing. However, qubits are magical because they can be in a superposition of states!

In simple terms:

- A classical bit can be either `0` or `1`.
- A qubit can be in a state |0⟩, |1⟩, or any superposition α|0⟩ + β|1⟩, where α and β are complex numbers.
- Note: This is in [Hilbert Space](https://en.wikipedia.org/wiki/Hilbert_space)

## Measuring a Qubit 🔍

When we measure a qubit, we "collapse" its superposition to one of the basis states:

- The probability of collapsing to |0⟩ is |α|<sup>2</sup>.
- The probability of collapsing to |1⟩ is |β|<sup>2</sup>.

### How It Works

1. **State Vector:** The qubit is in a state α|0⟩ + β|1⟩.
2. **Probabilities:** Calculate the probabilities |α|<sup>2</sup> and |β|<sup>2</sup>.
3. **Random Choice:** Use these probabilities to randomly choose the measurement outcome.

### Example in Python

<pre><code>
import numpy as np

class Ket:
    def __init__(self, alpha, beta):
        self.state_vector = np.array([alpha, beta], dtype=complex)

    def measure(self):
        probabilities = np.abs(self.state_vector) ** 2
        return np.random.choice([0, 1], p=probabilities)

# Example usage
alpha = 1/np.sqrt(2)
beta = 1/np.sqrt(2)
ket_instance = Ket(alpha, beta)
measurement_result = ket_instance.measure()
print(f"Measurement result: {measurement_result}")
</code></pre>
