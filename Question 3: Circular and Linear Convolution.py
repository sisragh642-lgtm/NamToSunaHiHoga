# Question 3: Circular and Linear Convolution
import numpy as np
from numpy.fft import fft, ifft

print("--- Question 3: Circular and Linear Convolution ---")

# Input sequences
x = np.array([1, 2, 3, 1])
h = np.array([1, 1, 1])

#  Circular Convolution 
h_padded = np.zeros(N)
h_padded[:len(h)] = h

X = fft(x)
H = fft(h_padded)
Y = X * H
y_circular = ifft(Y)

#  Linear Convolution 
y_linear = np.convolve(x, h)

# Results 
print("x(n):", x)
print("h(n):", h)
print("\nCircular Convolution y(n):", np.round(y_circular, 2))
print("Linear Convolution y(n):", y_linear)
