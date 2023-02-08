
#EXERCISE 4
float = ("decimal number")
integer = ("a whole number")

sequence = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(sequence)

# Method 1: Using a for loop to generate a sequence of floats
sequence = []
for x in range(15):
    sequence.append(1.5 + (x / 2))

print(sequence)