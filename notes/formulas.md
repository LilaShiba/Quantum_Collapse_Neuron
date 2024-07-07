# 🧙 Quantum Mechanics Study Sheet 🧙

## 🔮 Fundamental Constants

- **Planck's Constant**: $$\ h \approx 6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s} $$
  - *Planck's constant is a fundamental physical constant that relates the energy of a photon to its frequency. It is a cornerstone in quantum mechanics, highlighting the quantized nature of energy.*

- **Reduced Planck's Constant ($\hbar$)**: $ \hbar = \frac{h}{2\pi} \approx 1.0545718 \times 10^{-34} \ \text{J} \cdot \text{s} $

  - *Reduced Planck's constant, often called "h-bar," is used in many quantum mechanics equations. It simplifies the expression of quantum phenomena, especially angular momentum and the Heisenberg uncertainty principle.*

## ✨ Wave-Particle Duality

- **De Broglie Wavelength**:
  $$\lambda = \frac{h}{p}$$
  - $\lambda$ = wavelength
  - $h$ = Planck's constant
  - $p$ = momentum
  - *De Broglie's hypothesis states that every moving particle or object has an associated wave. This wave-particle duality is a fundamental concept of quantum mechanics.*

## 🪄 Wave Function

- **Schrödinger Equation (Time-Dependent)**:
  $$i \hbar \frac{\partial \psi(\mathbf{r}, t)}{\partial t} = \left( -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r}, t) \right) \psi(\mathbf{r}, t)$$
  - $ \psi(\mathbf{r}, t) $ = wave function
  - $ \nabla^2 $ = Laplacian operator
  - $ V(\mathbf{r}, t) $ = potential energy
  - $ m $ = mass
  - *The time-dependent Schrödinger equation describes how the quantum state of a physical system changes with time. It is the key equation of non-relativistic quantum mechanics.*

- **Schrödinger Equation (Time-Independent)**:
  $$\left( -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x) \right) \psi(x) = E \psi(x)$$
  - $ E $ = energy eigenvalue
  - *The time-independent Schrödinger equation is used to find the stationary states of a quantum system. These are states with a definite energy, which do not change over time.*

## 🧩 Operators and Observables

- **Hamiltonian Operator ($\hat{H}$)**:
  $$\hat{H} = -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r})$$
  - *The Hamiltonian operator represents the total energy of the system, including both kinetic and potential energies. It is used to determine the evolution of the system in time.*

- **Momentum Operator ($\hat{p}$)**:
  $$\hat{p} = -i \hbar \nabla$$
  - *The momentum operator is associated with the momentum of the particle. In quantum mechanics, momentum is an observable, and its operator acts on the wave function to give the momentum value.*

- **Position Operator ($\hat{x}$)**:
  $$\hat{x} = x$$
  - *The position operator simply represents the position variable. It is used to measure the position of a particle in a quantum system.*

## 🌟 Commutation Relations

- **Position and Momentum**:
  $$[\hat{x}, \hat{p}] = i \hbar$$
  - *The commutation relation between position and momentum operators is a fundamental result in quantum mechanics. It reflects the intrinsic uncertainty between these two observables, as described by the Heisenberg uncertainty principle.*

## 🌌 Heisenberg Uncertainty Principle

$$\Delta x \Delta p \geq \frac{\hbar}{2}$$

- *The Heisenberg uncertainty principle states that it is impossible to simultaneously know the exact position and momentum of a particle. The more precisely one is known, the less precisely the other can be known.*

## 🎲 Probability Density

- **Probability Density Function**:
  $$P(x) = |\psi(x)|^2$$
  - *The probability density function gives the probability of finding a particle at a specific position. It is the square of the absolute value of the wave function.*

- **Normalization Condition**:
  $$\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1$$
  - *The normalization condition ensures that the total probability of finding the particle in all space is 1, meaning the particle must be somewhere in the space.*

## 📚 Legend

- $h$: Planck's constant
- $\hbar$: Reduced Planck's constant
- $\lambda$: Wavelength
- $p$: Momentum
- $\psi$: Wave function
- $\nabla^2$: Laplacian operator
- $V$: Potential energy
- $m$: Mass
- $\hat{H}$: Hamiltonian operator
- $\hat{p}$: Momentum operator
- $\hat{x}$: Position operator
- $[\hat{x}, \hat{p}]$: Commutator of position and momentum operators
- $\Delta x$: Uncertainty in position
- $\Delta p$: Uncertainty in momentum
- $|\psi(x)|^2$: Probability density
- $\int$: Integral symbol
