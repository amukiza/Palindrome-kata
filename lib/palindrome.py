class Palindrome:

    def __init__(self, word):
        self.word = word

    def get_letter_at(self, index):
        return self.word.letter_at(index)

    def get_last_index(self):
        return self.word.last_index()

    def is_palindrome(self):
        end = self.get_last_index()
        start = 0
        while self._is_not_middle(start, end) and self._are_equal_at(start, end):
            start += 1
            end -= 1
        return self._is_middle(start, end)

    def _are_equal_at(self, index_1, index_2):
        return self.get_letter_at(index_1) is self.get_letter_at(index_2)

    def _is_middle(self, start, end):
        return end <= start

    def _is_not_middle(self, start, end):
        return start < end
