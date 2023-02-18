import random

# function reads the words from the given file and returns a list of words.
def get_words_from_file(sowpods):
    with open(sowpods) as file:
        words = file.read().split()
    return words

# function to select length number of random words from the words list and joins them into a sentence
def get_random_sentence(length, words):
    sentence = ' '.join(random.choices(words, k=length)).lower()
    sentence = sentence.capitalize() + '.'
    return sentence

def main():
    print("Welcome to the Random Sentence Generator!")
    sowpods = 'words.txt'
    words = get_words_from_file(sowpods)
    while True:
        try:
            length = int(input("How long would you like your sentence to be? (2-20): "))
            if length < 2 or length > 20:
                print("Invalid input. Please enter a number between 2 and 20.")
                continue
            sentence = get_random_sentence(length, words)
            print(sentence)
            break
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 20.")

if __name__ == '__main__':
    main()

