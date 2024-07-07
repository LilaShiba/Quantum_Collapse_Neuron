import math
import cmath

class Photon:
    def __init__(self, momentum):
        self.h = 6.62607015e-34  # Planck's constant in J·s
        self.hbar = self.h / (2 * math.pi)  # Reduced Planck's constant in J·s
        self.momentum = momentum  # momentum in kg·m/s
        self.wavelength = self.calculate_wavelength()
    
    def calculate_wavelength(self):
        """Calculate the De Broglie wavelength."""
        return self.h / self.momentum
    
    def schrodinger_eq_time_independent(self, potential_energy, position):
        """Solve the time-independent Schrödinger equation."""
        # Assumption: A simple one-dimensional potential well
        k = cmath.sqrt(2 * potential_energy / self.hbar**2)
        wave_function = cmath.exp(1j * k * position) + cmath.exp(-1j * k * position)
        return wave_function
    
    def probability_density(self, wave_function):
        """Calculate the probability density |ψ(x)|²."""
        return abs(wave_function)**2
    
    def normalize_wave_function(self, wave_function, positions):
        """Normalize the wave function over given positions."""
        normalization_factor = sum([self.probability_density(wave_function(x)) for x in positions])
        normalized_wave_function = wave_function / math.sqrt(normalization_factor)
        return normalized_wave_function

# Example usage:
momentum = 1e-27  # Example momentum in kg·m/s
photon = Photon(momentum)

print(f"Photon Wavelength: {photon.wavelength} meters")

# Example parameters for Schrödinger equation
potential_energy = 1e-20  # Example potential energy in Joules
position = 1e-10  # Example position in meters
wave_function = photon.schrodinger_eq_time_independent(potential_energy, position)
print(f"Wave Function at position {position}: {wave_function}")

probability = photon.probability_density(wave_function)
print(f"Probability Density at position {position}: {probability}")
