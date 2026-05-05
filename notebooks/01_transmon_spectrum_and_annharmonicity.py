# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

######
# Transmon Spectrum
######
N = 10
EC = 1.0
EJ_values = np.linspace(1, 50, 100)
energies = []

for EJ in EJ_values:
    # Charge basis Hamiltonian
    n_charges = np.arange(-N//2, N//2 + 1)
    n_op = qt.Qobj(np.diag(n_charges))
    N_actual = len(n_charges)
    cos_phi = 0.5 * (qt.qdiags([np.ones(N_actual-1)], 1) + 
                      qt.qdiags([np.ones(N_actual-1)], -1))
    H = 4 * EC * n_op**2 - EJ * cos_phi

    evals = H.eigenenergies()
    energies.append(evals[:5])  # keep lowest 5 levels

energies = np.array(energies)

plt.figure(figsize=(8,5))

for i in range(5):
    plt.plot(EJ_values, energies[:,i], label=f'Level {i}')
plt.xlabel('EJ/EC')
plt.ylabel('Energy')
plt.title('Transmon Spectrum (Charge Basis)')
plt.legend()
plt.show()

######
# Transmon Anharmonicity vs Ej/Ec
######

# Extract transition energies
E01 = energies[:, 1] - energies[:, 0]  # ground to first excited
E12 = energies[:, 2] - energies[:, 1]  # first to second excited

# Anharmonicity
alpha = E12 - E01

# Plot anharmonicity
plt.figure(figsize=(8, 5))
plt.plot(EJ_values, alpha, label='Anharmonicity α', color='blue')
plt.axhline(y=-EC, color='red', linestyle='--', label=f'-EC = -{EC}')
plt.xlabel('EJ/EC')
plt.ylabel('α (GHz)')
plt.title('Transmon Anharmonicity vs EJ/EC')
plt.legend()
plt.show()

# Print stabilized value
print(f"Anharmonicity at high EJ/EC: {alpha[-1]:.4f}")
print(f"Expected value -EC: {-EC:.4f}")