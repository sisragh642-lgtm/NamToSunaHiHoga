# Question 2: DFT and Frequency Response
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt

print("--- Question 2 ---")
x_2 = np.array([3, 4, 5, 6])
N_2 = len(x_2)

X_2 = fft(x_2)
print(f"x(n): {x_2}")
print(f"X(k): {X_2}")

k_2 = np.arange(N_2)
magnitude_2 = np.abs(X_2)
phase_2 = np.angle(X_2)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(k_2, magnitude_2)
plt.title('Question 2: Frequency Response (Magnitude)')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.stem(k_2, phase_2)
plt.title('Frequency Response (Phase)')
plt.xlabel('k (Frequency Index)')
plt.ylabel('Phase (radians)')
plt.tight_layout()
plt.show()
print("\n")
