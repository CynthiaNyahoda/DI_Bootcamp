from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator()

english_words = {}

for word in french_words:
    translation = translator.translate(word, dest='en')
    english_words[word] = translation.text

print(english_words)
