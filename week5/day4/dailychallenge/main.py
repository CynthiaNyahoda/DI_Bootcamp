# Create a class called Text that takes a string as an argument and store the text in a attribute

class Text:
    def __init__(self, text):
        self.text = text
  
#   a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message  # 
    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency == 0:
            return f"The word '{word}' is not present in the text."
        else:
            return f"The word '{word}' appears {frequency} time(s) in the text."
    
    # a method that returns the most common word in the text.
    
    def most_common_word(self):
        words = self.text.split()
        if not words:
            return "The text is empty."
        else:
            return max(set(words), key=words.count)
    
    # a method that returns a list of all the unique words in the text.

    def unique_words(self):
        words = self.text.split()
        if not words:
            return "The text is empty."
        else:
            return list(set(words))

text = Text("A good book would sometimes cost as much as a good house.")
print(text.word_frequency("good"))
print(text.most_common_word())
print(text.unique_words())


# PART II
class Text:
    def __init__(self, text):
        self.text = text
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            text = f.read()
        return cls(text)
    
    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency == 0:
            return f"The word '{word}' is not present in the text."
        else:
            return f"The word '{word}' appears {frequency} time(s) in the text."
    
    def most_common_word(self):
        words = self.text.split()
        if not words:
            return "The text is empty."
        else:
            return max(set(words), key=words.count)
    
    def unique_words(self):
        words = self.text.split()
        if not words:
            return "The text is empty."
        else:
            return list(set(words))

text = Text.from_file('the_stranger.txt')
print(text.most_common_word())
print(text.word_frequency("sun"))
print(text.unique_words())
