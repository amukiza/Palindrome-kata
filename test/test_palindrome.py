from unittest import TestCase
from lib.word import Word
from lib.palindrome import Palindrome


class TestPalindrome(TestCase):

    def test_get_letter_at(self):
        word = Word("noon")
        palindrome = Palindrome(word)

        self.assertEquals("n", palindrome.get_letter_at(0))

    def test_returns_legth_of_another_word(self):
        word = Word("Very Long word")
        palindrome = Palindrome(word)
        self.assertEquals("d", palindrome.get_letter_at(13))

    def test_is_palindrome(self):
        word = Word("noon")
        palindrome = Palindrome(word)
        self.assertTrue(palindrome.is_palindrome())

    def test_false_if_word_not_palindrome(self):
        word = Word("Boss")
        palindrome = Palindrome(word)
        self.assertFalse(palindrome.is_palindrome())

    def test_get_last_index(self):
        word = Word("Boss")
        palindrome = Palindrome(word)
        self.assertEquals(3, palindrome.get_last_index())

    def test_palindrome_word_with_odd_number_letters(self):
        word = Word("racecar")
        palindrome = Palindrome(word)
        self.assertTrue(palindrome.is_palindrome())