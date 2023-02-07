int_list = [0,1,2,3,4,5,6,7,8,9]
#modifyin
#adding stuff to list
print(f"starting length:{len(int_list)}") #getting length
int_list[0]+= 10 #incrementing


int_list.insert(0,-1)#add at the beginning

int_list.insert(7,100) #in between

int_list.append(-1) #add at the end

print(f" end length: {len(int_list)}")

int_list.remove(100)

#pop() using index



print(int_list)



unsorted_list = [ 5,8,7,3,"hello","hello", 3.8, 1,12]
print(unsorted_list)

#to sort
unsorted_list = [ 5,8,7,3, 3.8, 1,12]
print(sorted(unsorted_list)) #ascending

print(sorted(unsorted_list, reverse=True)) #descending


alpha_list_unsorted =["b","a","g","h"]
print(sorted(alpha_list_unsorted))


#EX
list1=[5,10,15,20,25,50,20]
#find 20
print(list1.index(20))

#finding all
indexes_of_20 =[]
number_of_removed_values = 0
while 20 in list1:
    index_of_first_20_found = list1.index(20) + number_of_removed_values
    indexes_of_20.append(index_of_first_20_found)
    list1.pop(indexes_of_20[-1]- number_of_removed_values)
    number_of_removed_values+= 1
    print(f"indexes of 20: {indexes_of_20}")



#tuples
my_tuple = (5,6,7)
print(my_tuple)
print(my_tuple[0])


a_turple = (10,20,30,40)
d,c,b,a = a_turple
print(a)
print(b)
print(c)



#accept a number from user and print its multiplication table

my_numb =int(input("enter a number: "))
for x in range(100):
 print(f"{my_numb} * {x+1} = {my_numb*(x+1)}")
 
 
 #to exit an infinite loop use control + z or c