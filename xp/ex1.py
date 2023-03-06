import numpy as np

def create_array(start, length, stop):
    return np.linspace(start, stop, length)

arr = create_array(6, 100, 6 + 4*(100-1))
print(arr)
