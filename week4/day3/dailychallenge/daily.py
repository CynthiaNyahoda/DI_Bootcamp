# Challenge 1
word = input("Enter a word: ")

# storing indexes of each letter
letter_indexes = {}

# Iterate over each letter in the word
for x, letter in enumerate(word):
  
    if letter not in letter_indexes:
        letter_indexes[letter] = [x]

    else:
        letter_indexes[letter].append(x)


print(letter_indexes)





# Challenge 2
# Store items with their prices
store_items = {
    "apple": 0.5,
    "banana": 0.25,
    "carrot": 0.75,
    "donut": 1.0
}

# Get the amount of money in the wallet
wallet_amount = float(input("Enter the amount of money in your wallet: "))

# Create a list of items that can be afford
affordable_items = []


for item, price in store_items.items():
  
    if price <= wallet_amount:
        affordable_items.append(item)
        wallet_amount -= price

# Sort the list of affordable items in alphabetical order
affordable_items.sort()


if affordable_items:
    print("You can afford:", affordable_items)
else:
    print("Nothing")

