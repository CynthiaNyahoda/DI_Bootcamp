#challenge 1
number = int(input("Enter a number: "))
length = int(input("Enter the desired length: "))

multiples = []
for i in range(1, length+1):
    multiple = number * i
    multiples.append(multiple)

print(multiples)

#challenge 2

string = input("Enter a string: ")

result = ""
for i in range(len(string)):
    if i == 0 or string[i] != string[i-1]:
        result += string[i]

print(result)

