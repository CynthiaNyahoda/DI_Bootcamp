#to handle errors use they "try catch" method
# use "dir" to find out the functions you can use for a certain element
#enumerate means counting or retrieving index things in a list
#enumerate replaces the "for functions" but its the same
#zip ties stuff together element by element
#list comprehension (short form of writting codes)



#to break and make

init_vlaur = 12345
rebuilt_value = 0

for index, character in enumerate(str(init_vlaur)):
    print(f"The index and values are : {index}, {character}")
    rebuilt_value += int(character)
print(f"the current value is: {rebuilt_value}")

