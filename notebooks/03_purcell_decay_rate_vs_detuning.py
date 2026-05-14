# Purcell decay simulation — standard vs filtered
# Purcell filter improves T1 by ~10^6x
# Purcell no longer limiting factor
# Real T1 limit: TLS defects, quasiparticles, materials losses
# EIT analogy: off-resonant driving suppresses absorption by same 1/Delta^2 scaling

import numpy as np
import matplotlib.pyplot as plt

g = 0.1
kappa = 0.01
kappa_filter = 0.001
Delta_filter = 1.0

Delta_values = np.linspace(0.1, 5.0, 200)

Gamma_P = (g / Delta_values)**2 * kappa
Gamma_P_filtered = Gamma_P * (kappa_filter/Delta_filter)**2

T1_standard = 1/Gamma_P
T1_filtered = 1/Gamma_P_filtered

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(Delta_values, Gamma_P, color='blue', label='Standard Purcell')
ax1.plot(Delta_values, Gamma_P_filtered, color='red', label='With Purcell Filter')
ax1.set_xlabel('Detuning Δ (GHz)')
ax1.set_ylabel('Purcell Decay Rate (GHz)')
ax1.set_title('Purcell Decay Rate vs Detuning')
ax1.set_yscale('log')
ax1.legend()

ax2.plot(Delta_values, T1_standard*1000, color='blue', label='T1 Standard (ns)')
ax2.plot(Delta_values, T1_filtered*1000, color='red', label='T1 Filtered (ns)')
ax2.set_xlabel('Detuning Δ (GHz)')
ax2.set_ylabel('T1 (ns)')
ax2.set_title('T1 Purcell Limit vs Detuning')
ax2.set_yscale('log')
ax2.legend()

plt.tight_layout()
plt.show()

print(f"T1 standard at Δ=1.0: {1/((g/1.0)**2 * kappa)*1000:.1f} ns")
print(f"T1 filtered at Δ=1.0: {1/((g/1.0)**2 * kappa * (kappa_filter/Delta_filter)**2)*1000:.1f} ns")
print(f"Improvement factor: {(kappa/kappa_filter)**2 * (Delta_filter)**2:.0f}x")
