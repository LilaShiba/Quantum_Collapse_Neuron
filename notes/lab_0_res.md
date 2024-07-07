# 🧙 Quantum Mechanics Practice Lab Submission 🧙

## 🔮 Fundamental Constants

### Exercise 1: Planck's Constant

1. **Theory**: Planck's constant ($h$) is a fundamental physical constant that represents the quantization of energy levels in quantum mechanics. It is the proportionality constant between the energy ($E$) of a photon and the frequency ($\nu$) of its associated electromagnetic wave, given by the equation $E = h\nu$. This "magic number" signifies the smallest possible unit of energy, highlighting the discrete nature of energy levels in quantum systems.

2. **Practical**:
   - Given: $\nu = 5 \times 10^{14}$ Hz
   - Planck's constant: $h \approx 6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s}$

   Calculation:
   \[
   E = h\nu = (6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s}) \times (5 \times 10^{14} \ \text{Hz}) = 3.313035075 \times 10^{-19} \ \text{J}
   \]

   Therefore, the energy of the photon is $3.313035075 \times 10^{-19}$ J.

### Exercise 2: Reduced Planck's Constant

1. **Theory**: The reduced Planck's constant ($\hbar$) is often more convenient to use in quantum mechanics because it simplifies equations involving angular momentum and wave functions. It is defined as $\hbar = \frac{h}{2\pi}$. Many quantum mechanical equations, such as the Schrödinger equation and commutation relations, are more succinct when expressed using $\hbar$.

2. **Practical**:
   \[
   \hbar = \frac{h}{2\pi} = \frac{6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s}}{2\pi} \approx 1.0545718 \times 10^{-34} \ \text{J} \cdot \text{s}
   \]

## ✨ Wave-Particle Duality

### Exercise 3: De Broglie Wavelength

1. **Theory**: Wave-particle duality is a fundamental concept in quantum mechanics which states that every particle or quantum entity can exhibit both wave-like and particle-like properties. This duality is crucial in understanding phenomena such as interference and diffraction, which cannot be explained by classical mechanics alone. The De Broglie hypothesis extends this concept by proposing that any moving particle has an associated wavelength, given by $\lambda = \frac{h}{p}$.

2. **Practical**:
   - Given: $m_e \approx 9.11 \times 10^{-31}$ kg, $v = 2 \times 10^6$ m/s
   - Planck's constant: $h \approx 6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s}$

   Calculation:
   \[
   p = mv = (9.11 \times 10^{-31} \ \text{kg}) \times (2 \times 10^6 \ \text{m/s}) = 1.822 \times 10^{-24} \ \text{kg} \cdot \text{m/s}
   \]
   \[
   \lambda = \frac{h}{p} = \frac{6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s}}{1.822 \times 10^{-24} \ \text{kg} \cdot \text{m/s}} \approx 3.64 \times 10^{-10} \ \text{m}
   \]

   Therefore, the De Broglie wavelength of the electron is approximately $3.64 \times 10^{-10}$ m.

## 🪄 Wave Function

### Exercise 4: Schrödinger Equation (Time-Dependent)

1. **Theory**: The time-dependent Schrödinger equation describes how the quantum state of a physical system evolves over time. It is a key equation in non-relativistic quantum mechanics, capturing the dynamics of particles in a potential field. The equation is:
   \[
   i \hbar \frac{\partial \psi(\mathbf{r}, t)}{\partial t} = \left( -\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{r}, t) \right) \psi(\mathbf{r}, t)
   \]
   This equation ensures that the wave function $\psi(\mathbf{r}, t)$ evolves in a manner consistent with the principles of quantum mechanics.

2. **Practical**:
   Given the initial wave function $ \psi(x, 0) = Ae^{-(x/a)^2} $, solve the time-dependent Schrödinger equation for a free particle.

   For a free particle, the potential $V = 0$, so the equation simplifies to:
   \[
   i \hbar \frac{\partial \psi(x, t)}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi(x, t)}{\partial x^2}
   \]

   Assuming the solution is of the form $\psi(x, t) = \phi(x) e^{-(iEt/\hbar)}$, substitute and solve:
   \[
   -\frac{\hbar^2}{2m} \frac{d^2 \phi(x)}{dx^2} = E \phi(x)
   \]
   \[
   \phi(x) = A e^{-(x/a)^2} \quad \text{(Gaussian form is retained)}
   \]

### Exercise 5: Schrödinger Equation (Time-Independent)

1. **Theory**: The time-independent Schrödinger equation describes the stationary states of a quantum system, where the probability distribution of the particle's position does not change with time. It is given by:
   \[
   \left( -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x) \right) \psi(x) = E \psi(x)
   \]

2. **Practical**:
   For a particle in a one-dimensional box of length $L$, the potential $V(x) = 0$ inside the box and $V(x) = \infty$ outside the box. The boundary conditions require $\psi(0) = \psi(L) = 0$.

   Solving the Schrödinger equation inside the box:
   \[
   \frac{d^2 \psi(x)}{dx^2} = -k^2 \psi(x) \quad \text{where} \quad k = \frac{\sqrt{2mE}}{\hbar}
   \]
   The general solution is:
   \[
   \psi(x) = A \sin(kx) + B \cos(kx)
   \]
   Applying the boundary conditions, we find:
   \[
   \psi(x) = A \sin\left(\frac{n\pi x}{L}\right), \quad n = 1, 2, 3, \ldots
   \]
   The corresponding energy eigenvalues are:
   \[
   E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}
   \]

## 🧩 Operators and Observables

### Exercise 6: Hamiltonian Operator

1. **Theory**: The Hamiltonian operator ($\hat{H}$) represents the total energy of a quantum system, including both kinetic and potential energies. It is crucial in determining the time evolution of the system through the Schrödinger equation.

2. **Practical**:
   For a harmonic oscillator with potential energy $V(x) = \frac{1}{2} m \omega^2 x^2$, the Hamiltonian operator is:
   \[
   \hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + \frac{1}{2} m \omega^2 x^2
   \]
   The energy eigenvalues are given by:
   \[
   E_n = \left(n + \frac{1}{2}\right) \hbar \omega, \quad n = 0, 1, 2, \ldots
   \]

### Exercise 7: Momentum Operator

1. **Theory**: The momentum operator $\hat{p} = -i \hbar \nabla$ relates to the particle's momentum. Applying it to the wave function gives the momentum value, reflecting the particle's movement in space.

2. **Practical**:
   Apply the momentum operator to a plane wave $\psi(x) = Ae^{ikx}$:
   \[
   \hat{p} \psi(x) = -i \hbar \frac{d}{dx} (Ae^{ikx}) = \hbar k \psi(x)
   \]
   Therefore, the momentum value is $\hbar k$.

### Exercise 8: Position Operator

1. **Theory**: The position operator $\hat{x} = x$ measures the position of a particle in a quantum system. It directly relates to the spatial coordinate in the wave function.

2. **Practical**:
   For a particle in a one-dimensional box of length $L$ in its ground state:
   \[
   \psi_1(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{\pi x}{L}\right)
   \]
   The expectation value of the position operator:
   \[
   \langle x \rangle = \int_0^L x |\psi_1(x)|^2 dx
   \]
   Calculation:
   \[
   \langle x \rangle = \int_0^L x \left(\frac{2}{L} \sin^2\left(\frac{\pi x}{L}\right)\right) dx = \frac{L}{2}
   \]
   Therefore, $\langle x \rangle = \frac{L}{2}$.

## 🌟 Commutation Relations

### Exercise 9: Position and Momentum

1. **Theory**: The commutation relation $[x̂, p̂] = i ħ$ expresses the fundamental quantum mechanical principle that position and momentum cannot be simultaneously measured with arbitrary precision. This underlies the Heisenberg uncertainty principle.

2. **Practical**:
   Verify the commutation relation by applying the operators $\hat{x}$ and $\hat{p}$ to a wave function $\psi(x)$:
   \[
   [\hat{x}, \hat{p}] \psi(x) = \hat{x} (\hat{p} \psi(x)) - \hat{p} (\hat{x} \psi(x))
   \]
   Applying $\hat{p} = -i \hbar \frac{d}{dx}$ and $\hat{x} = x$:
   \[
   \hat{p} \psi(x) = -i \hbar \frac{d \psi(x)}{dx}, \quad \hat{x} \psi(x) = x \psi(x)
   \]
   \[
   \hat{x} (\hat{p} \psi(x)) = -i \hbar x \frac{d \psi(x)}{dx}, \quad \hat{p} (\hat{x} \psi(x)) = -i \hbar \frac{d}{dx} (x \psi(x)) = -i \hbar \left( \psi(x) + x \frac{d \psi(x)}{dx} \right)
   \]
   \[
   [\hat{x}, \hat{p}] \psi(x) = -i \hbar x \frac{d \psi(x)}{dx} + i \hbar \left( \psi(x) + x \frac{d \psi(x)}{dx} \right) = i \hbar \psi(x)
   \]
   Therefore, $[\hat{x}, \hat{p}] = i \hbar$.

## 🌌 Heisenberg Uncertainty Principle

### Exercise 10: Uncertainty Principle

1. **Theory**: The Heisenberg uncertainty principle states that it is impossible to simultaneously know the exact position and momentum of a particle. The principle is mathematically expressed as $\Delta x \Delta p \geq \frac{\hbar}{2}$. This principle implies a fundamental limit to the precision of measurements, reflecting the intrinsic quantum nature of particles.

2. **Practical**:
   Given a Gaussian wave packet with standard deviation $\Delta x$ in position, the corresponding uncertainty in momentum $\Delta p$ is calculated as:
   \[
   \Delta p \approx \frac{\hbar}{2 \Delta x}
   \]
   Verify:
   \[
   \Delta x \Delta p \geq \frac{\hbar}{2}
   \]

## 🎲 Probability Density

### Exercise 11: Probability Density Function

1. **Theory**: The probability density function $P(x) = |ψ(x)|²$ represents the probability of finding a particle at a specific position $x$ in space. It is derived from the wave function and provides a probabilistic interpretation of the particle's location.

2. **Practical**:
   For a particle in a one-dimensional box of length $L$, the ground state wave function is:
   \[
   \psi_1(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{\pi x}{L}\right)
   \]
   The probability density function:
   \[
   P(x) = |\psi_1(x)|^2 = \left( \sqrt{\frac{2}{L}} \sin\left(\frac{\pi x}{L}\right) \right)^2 = \frac{2}{L} \sin^2\left(\frac{\pi x}{L}\right)
   \]
   Plot:
   ![Probability Density Function](https://via.placeholder.com/600x400?text=Probability+Density+Function)

### Exercise 12: Normalization Condition

1. **Theory**: Normalization ensures that the total probability of finding the particle in all space is 1. This condition guarantees that the particle exists somewhere in the defined space, making the wave function a valid probability distribution.

2. **Practical**:
   Normalize the wave function $\psi(x) = A e^{-(x/a)^2}$ over all space:
   \[
   \int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1
   \]
   \[
   \int_{-\infty}^{\infty} A^2 e^{-2(x/a)^2} dx = 1
   \]
   Solving for $A$:
   \[
   A^2 \int_{-\infty}^{\infty} e^{-2(x/a)^2} dx = 1
   \]
   Using the Gaussian integral $\int_{-\infty}^{\infty} e^{-2(x/a)^2} dx = \sqrt{\frac{\pi a^2}{2}}$:
   \[
   A^2 \sqrt{\frac{\pi a^2}{2}} = 1 \implies A = \left(\frac{2}{a \sqrt{\pi}}\right)^{1/2}
   \]
   Therefore, $A = \sqrt{\frac{2}{a \sqrt{\pi}}}$.

## 📚 Legend

- $ h $: Planck's constant
- $ \hbar $: Reduced Planck's constant
- $ \lambda $: Wavelength
- $ p $: Momentum
- $ \psi $: Wave function
- $ \nabla^2 $: Laplacian operator
- $ V $: Potential energy
- $ m $: Mass
- $ \hat{H} $: Hamiltonian operator
- $ \hat{p} $: Momentum operator
- $ \hat{x} $: Position operator
- $ [x̂, p̂] $: Commutator of position and momentum operators
- $ Δx $: Uncertainty in position
- $ Δp $: Uncertainty in momentum
- $ |ψ(x)|² $: Probability density
- $ ∫ $: Integral symbol
