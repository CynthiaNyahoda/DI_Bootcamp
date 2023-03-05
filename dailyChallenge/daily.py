import random

# Create a table of size M x N filled with random integers between 1 and 100
M = random.randint(2, 50)
N = random.randint(2, 39) + 1
table = [[random.randint(1, 100) for j in range(N)] for i in range(M)]

# Print out the third row
print(table[2])

# Print out the third column
print([table[i][2] for i in range(M)])

# Set every element in the last row equal to 7
for j in range(N):
    table[-1][j] = 7

# Set every element in the last column equal the sum of the first two columns
col_sum = [sum(table[i][0:2]) for i in range(M)]
for i in range(M):
    table[i][-1] = col_sum[i]

print(table)


# USING NUMPY
import numpy as np

# Create a table of size M x N filled with random integers between 1 and 100
M = np.random.randint(2, 50)
N = np.random.randint(2, 39) + 1
table = np.random.randint(1, 101, size=(M, N))

# Print out the third row
print(table[2,:])

# Print out the third column
print(table[:,2])

# Set every element in the last row equal to 7
table[-1,:] = 7

# Set every element in the last column equal the sum of the first two columns
col_sum = np.sum(table[:,0:2], axis=1)
table[:,-1] = col_sum

print(table)
