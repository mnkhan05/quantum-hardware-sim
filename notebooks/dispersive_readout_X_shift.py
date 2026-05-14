# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:02:52 2026

@author: mnkha
"""

import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# Parameters
wr = 5.0      # resonator frequency (GHz)
wq = 4.0      # qubit frequency (GHz)
g = 0.1       # coupling strength (GHz)
kappa = 0.01  # resonator decay rate

# Detuning and chi
Delta = wq - wr
chi = g**2 / Delta

# Drive frequencies to probe
drive_freqs = np.linspace(wr - 0.5, wr + 0.5, 200)

# Lorentzian transmission for qubit in |0> and |1>
transmission_g = kappa**2 / ((drive_freqs - (wr + chi))**2 + kappa**2)
transmission_e = kappa**2 / ((drive_freqs - (wr - chi))**2 + kappa**2)

plt.figure(figsize=(8,5))
plt.plot(drive_freqs, transmission_g, label='Qubit |0⟩', color='blue')
plt.plot(drive_freqs, transmission_e, label='Qubit |1⟩', color='red')
plt.axvline(x=wr, color='gray', linestyle='--', label='Bare ωr')
plt.xlabel('Drive Frequency (GHz)')
plt.ylabel('Transmission')
plt.title('Dispersive Readout — χ Shift')
plt.legend()
plt.show()

print(f"χ = g²/Δ = {chi:.4f} GHz")
print(f"Total frequency split = {2*abs(chi):.4f} GHz")