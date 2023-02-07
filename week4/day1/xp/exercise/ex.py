#EXERCISE 1
print("Hello World"*4)

#EXERCISE 2
result = (99^3)*8
print(result)

#EXERCISE 3
5 < 3
False

3 == 3
True

3 == "3"
False

#"3" > 3
#False

"Hello" == "Hello"
True


#EXERCISE 4
computer_brand = "Glacy"
print("i have a", computer_brand, "computer")



#EXERCISE 5
name = "Cynthia"
age = 21
shoe_size = 3
infor = "my name is", name, "a short", age,"year old with a foot that fits in a shoe size", shoe_size
print(infor)


#EXERCISE 6
a = 6
b = 2

if a > b:
    print("Hello World")
    
    #EXERCISE 7
    number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


#EXERCISE 8
user_name = input("whats your name?: ")
my_name = "Cynthia"
if user_name == my_name:
    print("WE HAVE THE SAME NAME!!!")
else: 
    print("well thats a bammer")
    
    
    #EXERCISE 9
min_height_inches = 57   #145cm divided by 2.54
user_height_inches = int(input("What is your height in inches? "))

if user_height_inches >= min_height_inches:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")

