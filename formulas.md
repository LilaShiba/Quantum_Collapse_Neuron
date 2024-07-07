<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="styles.css">

</head>
<body>

<h1>🧙 Quantum Mechanics Study Sheet 🧙</h1>

<h2>🔮 Fundamental Constants</h2>

<ul>
    <li><strong>Planck's Constant ($h$)</strong>: $h \approx 6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s}$</li>
    <ul>
        <li><em>Planck's constant is a fundamental physical constant that relates the energy of a photon to its frequency. It is a cornerstone in quantum mechanics, highlighting the quantized nature of energy.</em></li>
    </ul>
    <li><strong>Reduced Planck's Constant ($\hbar$)</strong>: $\hbar = \frac{h}{2\pi} \approx 1.0545718 \times 10^{-34} \ \text{J} \cdot \text{s}$</li>
    <ul>
        <li><em>Reduced Planck's constant, often called "h-bar," is used in many quantum mechanics equations. It simplifies the expression of quantum phenomena, especially angular momentum and the Heisenberg uncertainty principle.</em></li>
    </ul>
</ul>

<h2>✨ Wave-Particle Duality</h2>

<ul>
    <li><strong>De Broglie Wavelength</strong>:</li>
    <p>$$\lambda = \frac{h}{p}$$</p>
    <ul>
        <li>$\lambda$ = wavelength</li>
        <li>$h$ = Planck's constant</li>
        <li>$p$ = momentum</li>
        <li><em>De Broglie's hypothesis states that every moving particle or object has an associated wave. This wave-particle duality is a fundamental concept of quantum mechanics.</em></li>
    </ul>
</ul>

<h2>🪄 Wave Function</h2>

<ul>
    <li><strong>Schrödinger Equation (Time-Dependent)</strong>:</li>
    <p>$$i \hbar \frac{\partial \psi(\mathbf{r}, t)}{\partial t} = \left( -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r}, t) \right) \psi(\mathbf{r}, t)$$</p>
    <ul>
        <li>$\psi(\mathbf{r}, t)$ = wave function</li>
        <li>$\nabla^2$ = Laplacian operator</li>
        <li>$V(\mathbf{r}, t)$ = potential energy</li>
        <li>$m$ = mass</li>
        <li><em>The time-dependent Schrödinger equation describes how the quantum state of a physical system changes with time. It is the key equation of non-relativistic quantum mechanics.</em></li>
    </ul>
    <li><strong>Schrödinger Equation (Time-Independent)</strong>:</li>
    <p>$$\left( -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x) \right) \psi(x) = E \psi(x)$$</p>
    <ul>
        <li>$E$ = energy eigenvalue</li>
        <li><em>The time-independent Schrödinger equation is used to find the stationary states of a quantum system. These are states with a definite energy, which do not change over time.</em></li>
    </ul>
</ul>

<h2>🧩 Operators and Observables</h2>

<ul>
    <li><strong>Hamiltonian Operator ($\hat{H}$)</strong>:</li>
    <p>$$\hat{H} = -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r})$$</p>
    <ul>
        <li><em>The Hamiltonian operator represents the total energy of the system, including both kinetic and potential energies. It is used to determine the evolution of the system in time.</em></li>
    </ul>
    <li><strong>Momentum Operator ($\hat{p}$)</strong>:</li>
    <p>$$\hat{p} = -i \hbar \nabla$$</p>
    <ul>
        <li><em>The momentum operator is associated with the momentum of the particle. In quantum mechanics, momentum is an observable, and its operator acts on the wave function to give the momentum value.</em></li>
    </ul>
    <li><strong>Position Operator ($\hat{x}$)</strong>:</li>
    <p>$$\hat{x} = x$$</p>
    <ul>
        <li><em>The position operator simply represents the position variable. It is used to measure the position of a particle in a quantum system.</em></li>
    </ul>
</ul>

<h2>🌟 Commutation Relations</h2>

<ul>
    <li><strong>Position and Momentum</strong>:</li>
    <p>$$[\hat{x}, \hat{p}] = i \hbar$$</p>
    <ul>
        <li><em>The commutation relation between position and momentum operators is a fundamental result in quantum mechanics. It reflects the intrinsic uncertainty between these two observables, as described by the Heisenberg uncertainty principle.</em></li>
    </ul>
</ul>

<h2>🌌 Heisenberg Uncertainty Principle</h2>

<p>$$\Delta x \Delta p \geq \frac{\hbar}{2}$$</p>

<ul>
    <li><em>The Heisenberg uncertainty principle states that it is impossible to simultaneously know the exact position and momentum of a particle. The more precisely one is known, the less precisely the other can be known.</em></li>
</ul>

<h2>🎲 Probability Density</h2>

<ul>
    <li><strong>Probability Density Function</strong>:</li>
    <p>$$P(x) = |\psi(x)|^2$$</p>
    <ul>
        <li><em>The probability density function gives the probability of finding a particle at a specific position. It is the square of the absolute value of the wave function.</em></li>
    </ul>
    <li><strong>Normalization Condition</strong>:</li>
    <p>$$\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1$$</p>
    <ul>
        <li><em>The normalization condition ensures that the total probability of finding the particle in all space is 1, meaning the particle must be somewhere in the space.</em></li>
    </ul>
</ul>

<h2>📚 Legend</h2>

<ul>
    <li>$h$: Planck's constant</li>
    <li>$\hbar$: Reduced Planck's constant</li>
    <li>$\lambda$: Wavelength</li>
    <li>$p$: Momentum</li>
    <li>$\psi$: Wave function</li>
    <li>$\nabla^2$: Laplacian operator</li>
    <li>$V$: Potential energy</li>
    <li>$m$: Mass</li>
    <li>$\hat{H}$: Hamiltonian operator</li>
    <li>$\hat{p}$: Momentum operator</li>
    <li>$\hat{x}$: Position operator</li>
    <li>$[\hat{x}, \hat{p}]$: Commutator of position and momentum operators</li>
    <li>$\Delta x$: Uncertainty in position</li>
    <li>$\Delta p$: Uncertainty in momentum</li>
    <li>$|\psi(x)|^2$: Probability density</li>
    <li>$\int$: Integral symbol</li>
</ul>

</body>
</html>
