class Anagram:
    def __init__(self, word):
        self.word_letters = sorted(word)

    def match(self, word_list):
        return [word for word in word_list if sorted(word) == self.word_letters]
