users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

disney_users_A = {}
for i in range(len(users)):
    disney_users_A[users[i]] = i

print(disney_users_A)

# 2. Use a for loop to recreate the 2nd result. 
disney_users_B = {}
for i in range(len(users)):
    disney_users_B[i] = users[i]
print(disney_users_B)

# 3. Use a method to recreate the 3rd result. The 3rd result is sorted alphabetically.
disney_users = {}
for i in range(len(users)):
    disney_users[users[i]] = i
    
disney_users_C = dict(sorted(disney_users.items()))
print(disney_users_C)

# 4. Only recreate the 1st result for:
# a. The characters, which names contain the letter “i”.
disney_users_A = {}
for x in range(len(users)):
    if 'i' in users[x]:
        disney_users_A[users[x]] = x
print(disney_users_A)

# b. The characters, which names start with the letter “m” or “p”.
disney_users_A = {}
for x in range(len(users)):
    if users[1][0] in ['m', 'p']:
        disney_users_A[users[x]] = x
print(disney_users_A)

