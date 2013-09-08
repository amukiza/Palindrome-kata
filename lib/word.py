class Word:

    def __init__(self, letters):
        self.letters = letters

    def letter_at(self, index):
        return self.letters[index]

    def length(self):
        return len(self.letters)

    def last_index(self):
        return len(self.letters) - 1