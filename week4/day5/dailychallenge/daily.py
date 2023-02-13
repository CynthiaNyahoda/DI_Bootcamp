def sort_words(words):
    words_list = words.split(',')
    sorted_list = [word.strip() for word in sorted(words_list)]
    return ','.join(sorted_list)

words = input("Enter words separated by commas: ")
print("Sorted words:", sort_words(words))
