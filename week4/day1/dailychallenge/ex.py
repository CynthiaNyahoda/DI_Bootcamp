string = input("Enter a string: ")

if len(string) == 10:
    print("String is 10 characters long.")
elif len(string) < 10:
    print("String not long enough.")
else:
    print("String too long.")


print("First character:", string[0])
print("Last character:", string[-1])


for i in range(len(string)):
    print(string[i])

string = list(string)
string[0], string[-1] = string[-1], string[0]
string[1], string[-2] = string[-2], string[1]
string = "".join(string)

print("Jumbled string:")
for i in range(len(string)):
    print(string[i])




