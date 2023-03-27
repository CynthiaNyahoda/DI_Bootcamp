class AnagramChecker:
    def __init__(self, wordlist_file):
        with open(wordlist_file, 'r') as f:
            self.wordlist = set([word.strip().lower() for word in f.readlines()])

    def is_valid_word(self, word):
        return word.strip().isalpha() and word.strip().lower() in self.wordlist

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        return [w for w in self.wordlist if self.is_anagram(word, w) and word.lower() != w.lower()]
