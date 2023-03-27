import os
from anagram_checker import AnagramChecker

def main():
    # Load word list
    wordlist_file = 'wordlist.txt'
    if not os.path.isfile(wordlist_file):
        print(f"Word list file {wordlist_file} not found")
        return

    # Create anagram checker
    anagram_checker = AnagramChecker(wordlist_file)

    # Show menu
    while True:
        print("Anagram Checker")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Enter your choice: ")

        # Input word
        if choice == '1':
            word = input("Enter a word: ").strip()
            if len(word.split()) > 1:
                print("Error: Only a single word is allowed")
                continue
            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed")
                continue

            # Checking if word is valid
            if not anagram_checker.is_valid_word(word):
                print(f"{word} is not a valid word")
                continue

            # Get anagrams
            anagrams = anagram_checker.get_anagrams(word)
            if len(anagrams) == 0:
                print(f"No anagrams found for {word}")
            else:
                print(f"Anagrams for {word}:")
                for a in anagrams:
                    print(a)
        # Exit program
        elif choice == '2':
            print("Goodbye!")
            break
        # Invalid choice
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
