<link rel="stylesheet" type="text/css" href="styles.css">

# 🧙‍♀️✨ Qubits Neuron Class 🚀🌌


![Hamiltonian Graph with Super Clusters](imgs/hamiltonian.png)
#### Hamiltonian Graph with Super Clusters

The goal is to incorporate quantum holographic properties inside a simulated CNN

<h2>What is a Qubit? 🧩</h2>

<p>A qubit is the basic unit of quantum information, just like a bit in classical computing. However, qubits are magical because they can be in a superposition of states!</p>

<p>In simple terms:</p>

<ul>
  <li>A classical bit can be either <code>0</code> or <code>1</code>.</li>
  <li>A qubit can be in a state |0⟩, |1⟩, or any superposition α|0⟩ + β|1⟩ where α and β are complex numbers.</li>
  <li>Note: This is in <a href="https://en.wikipedia.org/wiki/Hilbert_space">Hilbert Space</a>.</li>
  <li>Note: Layer class demands a Hamiltioan <a href='https://en.wikipedia.org/wiki/Hamiltonian_path'> Graph</a></li>
  <li>Note: Ideally and for ease sake this is an <a href='https://en.wikipedia.org/wiki/Orthonormality'> Orthonormal relationship </a></li>
</ul>

<p>Source: 1.) <a href="https://mitpressbookstore.mit.edu/book/9780262526678">MIT: A Gentle Introduction to Quantum Computing</a></p>

<p> Source: 2.) <a href="https://mitpressbookstore.mit.edu/book/9780262038430">MIT: Holographic Quantum Matter</a></p>



## Measuring a Qubit 🔍

<p>When we measure a qubit, we "collapse" its superposition to one of the basis states:</p>

<ul>
  <li>The probability of collapsing to |0⟩ is |α|<sup>2</sup>.</li>
  <li>The probability of collapsing to |1⟩ is |β|<sup>2</sup>.</li>
</ul>

<h3>How It Works</h3>

<ol>
  <li><strong>State Vector:</strong> The qubit is in a state α|0⟩ + β|1⟩.</li>
  <li><strong>Probabilities:</strong> Calculate the probabilities |α|<sup>2</sup> and |β|<sup>2</sup>.</li>
  <li><strong>Random Choice:</strong> Use these probabilities to randomly choose the measurement outcome.</li>
</ol>


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
