import math
import numpy as np

# Read the matrix
rows = int(input())
columns = int(input())
W = []
for i in range(rows):
  row = list(map(int, input().split()))
  W.append(row)
W = np.matrix(W)
print("W = ")
print(W)
n = columns

# A dictionary that keeps track of all bin sizes
b = {}

# Used to construct the vectors
shifts = np.arange(n)

# Loop through all n dimensional {0,1}-vectors u
for i in range(0, 2**(n)):

  # Get the vector u
  u = (i >> shifts) % 2

  # Compute the vector Wu and convert it into a tuple
  s = tuple(np.squeeze(np.asarray(W.dot(u))))

  # Increase the bin size of Wu by 1
  b[s] = b.get(s, 0) + 1

# Compute the normalized maximum bin size
maximum_bin_size = max(b.values())
normalized_maximum_bin_size = math.log2(maximum_bin_size)/n
print("Normalized maximum bin size: %.8f" % normalized_maximum_bin_size)

# Compute the normalized entropy
entropy_sum = 0
for sz in b.values():
  entropy_sum -= sz * (math.log2(sz) - n)
normalized_entropy = entropy_sum / (n*(2**n))
print("Normalized entropy:          %.8f" % normalized_entropy)

# Apply Theorem 1
beta_w = math.floor((normalized_maximum_bin_size+normalized_entropy-1)*1e5)/1e5
print("\nBy Theorem 1 it follows that for all ε > 0 there exists a vector w with\n  α(w) ≥ 2^((1-ε) n)\nand\n  β(w) ≥ 2^(%.5f n)" % beta_w)
