# 🧙 Quantum Mechanics Study Sheet 🧙

## 🔮 Fundamental Constants

- **Planck's Constant ($h$)**: $ h \approx 6.62607015 \times 10^{-34} \ \text{J} \cdot \text{s} $
  - *Planck's constant is a fundamental physical constant that relates the energy of a photon to its frequency. It is a cornerstone in quantum mechanics, highlighting the quantized nature of energy.*

- **Reduced Planck's Constant ($\hbar$)**: $ \hbar = \frac{h}{2\pi} \approx 1.0545718 \times 10^{-34} \ \text{J} \cdot \text{s} $
  - *Reduced Planck's constant, often called "h-bar," is used in many quantum mechanics equations. It simplifies the expression of quantum phenomena, especially angular momentum and the Heisenberg uncertainty principle.*

## ✨ Wave-Particle Duality

- **De Broglie Wavelength**:
  <pre><code>λ = h / p</code></pre>
  - $\lambda$ = wavelength
  - $h$ = Planck's constant
  - $p$ = momentum
  - *De Broglie's hypothesis states that every moving particle or object has an associated wave. This wave-particle duality is a fundamental concept of quantum mechanics.*

## 🪄 Wave Function

- **Schrödinger Equation (Time-Dependent)**:
  <pre><code>i ħ ∂ψ(r, t) / ∂t = ( -ħ² / 2m ∇² + V(r, t) ) ψ(r, t)</code></pre>
  - $ \psi(\mathbf{r}, t) $ = wave function
  - $ \nabla^2 $ = Laplacian operator
  - $ V(\mathbf{r}, t) $ = potential energy
  - $ m $ = mass
  - *The time-dependent Schrödinger equation describes how the quantum state of a physical system changes with time. It is the key equation of non-relativistic quantum mechanics.*

- **Schrödinger Equation (Time-Independent)**:
  <pre><code>( -ħ² / 2m d² / dx² + V(x) ) ψ(x) = E ψ(x)</code></pre>
  - $ E $ = energy eigenvalue
  - *The time-independent Schrödinger equation is used to find the stationary states of a quantum system. These are states with a definite energy, which do not change over time.*

## 🧩 Operators and Observables

- **Hamiltonian Operator ($\hat{H}$)**:
  <pre><code>Ĥ = -ħ² / 2m ∇² + V(r)</code></pre>
  - *The Hamiltonian operator represents the total energy of the system, including both kinetic and potential energies. It is used to determine the evolution of the system in time.*

- **Momentum Operator ($\hat{p}$)**:
  <pre><code>p̂ = -i ħ ∇</code></pre>
  - *The momentum operator is associated with the momentum of the particle. In quantum mechanics, momentum is an observable, and its operator acts on the wave function to give the momentum value.*

- **Position Operator ($\hat{x}$)**:
  <pre><code>x̂ = x</code></pre>
  - *The position operator simply represents the position variable. It is used to measure the position of a particle in a quantum system.*

## 🌟 Commutation Relations

- **Position and Momentum**:
  <pre><code>[x̂, p̂] = i ħ</code></pre>
  - *The commutation relation between position and momentum operators is a fundamental result in quantum mechanics. It reflects the intrinsic uncertainty between these two observables, as described by the Heisenberg uncertainty principle.*

## 🌌 Heisenberg Uncertainty Principle

<pre><code>Δx Δp ≥ ħ / 2</code></pre>

- *The Heisenberg uncertainty principle states that it is impossible to simultaneously know the exact position and momentum of a particle. The more precisely one is known, the less precisely the other can be known.*

## 🎲 Probability Density

- **Probability Density Function**:
  <pre><code>P(x) = |ψ(x)|²</code></pre>
  - *The probability density function gives the probability of finding a particle at a specific position. It is the square of the absolute value of the wave function.*

- **Normalization Condition**:
  <pre><code>∫ |ψ(x)|² dx = 1</code></pre>
  - *The normalization condition ensures that the total probability of finding the particle in all space is 1, meaning the particle must be somewhere in the space.*

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
