<link rel="stylesheet" type="text/css" href="styles.css">

# [What is Light?](https://youtu.be/7UuUOXfiz9Q?si=eZvPbhvttn-waPDz)

By the end of this lab, you will be able to explain the quantum properties of light using either Dirac Notation, experimentation results, or graphs produced by your own program.

## 🪄 Photons: The Tricksters of Light 🪄

Photons are the tiny particles that make up light, but they don't always play by the rules we expect! 🌟🔍 Unlike arrows that fly straight and true, photons can be in multiple places at once, interfere with themselves, and even communicate faster than the speed of light! 🚀✨ Let's explore some of these magical behaviors through the lens of quantum computing.

## 🔍 Understanding Vectors 🔍

Before we dive deeper into our quantum adventure, let's take a moment to understand vectors, which are fundamental to quantum computing.

### What is a Vector?
A vector is a quantity that has both magnitude (size) and direction. Think of it as an arrow: the length of the arrow represents the magnitude, and the way it points represents the direction.

![Layer 3](https://github.com/LilaShiba/Quantum_Collapse_Neuron/blob/main/imgs/qubit_ex.png)

### How Do We Use Vectors in Quantum Computing?
In quantum computing, vectors help us represent quantum states. For example, a single qubit (the basic unit of quantum information) can be represented as a vector in a two-dimensional space. This vector tells us the probabilities of the qubit being in different states.

### Vectors in Bra-Ket Notation
<details>
    <summary>Braket Notation in Quantum Mechanics 🧙‍♀️🔮</summary>
    <br>
    <p>In quantum mechanics, <a href='https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation'>bra-ket notation</a> is essential for representing quantum states and operations.</p>
    <ul>
        <li><strong>Ket |α⟩</strong>: Represents a quantum state vector. Example: |α⟩ could denote the state of a particle. 🌌</li>
        <li><strong>Bra ⟨β|</strong>: The conjugate transpose of a ket, helps for quick computations over all state space. 🔄</li>
        <li><strong>Inner Product ⟨β|α⟩</strong>: Represents the probability amplitude between states |β⟩ and |α⟩. ✨</li>
        <li><strong>Outer Product |α⟩⟨β|</strong>: An operator that projects onto the state |α⟩. 🌀</li>
    </ul>
    <p>Example in a qubit system:</p>
    <ul>
        <li><strong>Kets</strong>: |0⟩, |1⟩</li>
        <li><strong>Bras</strong>: ⟨0|, ⟨1|</li>
        <li><strong>Inner Product</strong>: ⟨0|1⟩ = 0 (shows orthogonality) 🌠</li>
        <li><strong>Outer Product</strong>: |0⟩⟨0| (a projection operator) 🌙</li>
    </ul>
</details>

## 🧪 Experiment: Polarized Light and Quantum States 🧪

Now, let's tie this understanding of vectors into our experiment. We'll be passing light through three layers of polarized film to demonstrate quantum properties.

#### What Are Polarized Films?
Polarized films are materials that only allow light waves vibrating in a certain direction to pass through. When light passes through these films, its direction (or polarization state) changes, much like how vectors can change direction.

---

# Our Experiment

<details>
<summary><strong>Start Lab Here!</strong></summary>
<br>
  
0. **Hardware:** Create a program to measure light in lux using Python & the Raspberry Pi.

 ![image](https://cdn-learn.adafruit.com/assets/assets/000/109/050/medium640/adafruit_products_VEML7700_RasPi_original.jpg?1645044837)

1. **Layer 1:** The first layer of polarized film will align the photons in a specific direction.

  ![Layer 1](https://alienryderflex.com/polarizer/01.gif)

2. **Layer 2:** The second layer, oriented at a different angle, will alter the photons' directions further.

  ![Layer 2](https://alienryderflex.com/polarizer/02.gif)
  
3. **Layer 3:** The third layer will demonstrate how the final direction of the photons is influenced by the previous two layers.

  ![Layer 3](https://alienryderflex.com/polarizer/03.gif)

### Connecting to Vectors
Think of the polarization of light as a vector. Each layer of polarized film changes the direction of this vector. By observing the changes in light intensity and direction after each layer, we can visualize how vectors (quantum states) are manipulated in quantum computing.

![Explanation In Math](https://github.com/LilaShiba/Quantum_computing_lab/assets/13423696/9452116e-fabf-44e4-90ce-3b4bd422b2c4)

### Observing Quantum Behavior
As we pass light through these three layers of polarized film, we observe a phenomenon where the addition of a third filter at a specific angle can allow more light to pass through. Here's how it works:

1. **Polarization Alignment**: 
   - The first polarized filter aligns incoming light waves along a specific polarization direction. Only light waves vibrating in this aligned direction can pass through, while others are blocked.

2. **Further Filtering**:
   - The second filter, oriented at a different angle relative to the first, further restricts the passage of light. It only allows light waves that align with its specific polarization orientation to pass through.

3. **Introducing the Third Filter**:
   - When we add a third filter at a particular angle relative to the first two, it introduces a new polarization direction. This angle is crucial because it can align with some of the previously blocked light waves that were restricted by the orientations of the first two filters.

4. **Enhanced Transmission**:
   - As a result, some of the light that was initially blocked by the first two filters can now pass through the third filter. This is because the third filter's angle allows it to transmit light waves that match its polarization orientation, effectively 'unblocking' certain light paths.

5. **Quantum Analogies**:
   - This behavior resembles quantum superposition, where particles like photons can exist in multiple states simultaneously until observed. In the context of quantum computing, this scenario illustrates how qubits can be manipulated to change their states, akin to how the polarization state of light changes with each additional filter.

In essence, the addition of a third polarized filter at a specific angle alters the available paths for light transmission by introducing a new polarization direction that aligns with previously blocked light waves. This phenomenon demonstrates the intricate relationship between polarization angles and light transmission, drawing parallels to quantum principles such as superposition and state manipulation.

</details>

# Resources / Works Cited
- [Hardware Setup](https://www.adafruit.com/product/4162)
- [Best Book on QC](https://mitpress.mit.edu/9780262526678/quantum-computing/)
