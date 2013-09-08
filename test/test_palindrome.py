from unittest import TestCase
from lib.word import Word
from lib.palindrome import Palindrome
from hamcrest import *


class TestPalindrome(TestCase):

    def test_get_letter_at(self):
        word = Word("noon")
        palindrome = Palindrome(word)
        
        assert_that(palindrome.get_letter_at(0), is_("n"))

    def test_returns_legth_of_another_word(self):
        word = Word("Very Long word")
        palindrome = Palindrome(word)
        assert_that(palindrome.get_letter_at(13), is_("d"))

    def test_is_palindrome(self):
        word = Word("noon")
        palindrome = Palindrome(word)
        assert_that(palindrome.is_palindrome(), is_(True))

    def test_false_if_word_not_palindrome(self):
        word = Word("Boss")
        palindrome = Palindrome(word)
        assert_that(palindrome.is_palindrome(), is_(False))

    def test_get_last_index(self):
        word = Word("Boss")
        palindrome = Palindrome(word)
        assert_that(palindrome.get_last_index(), is_(3))

    def test_palindrome_word_with_odd_number_letters(self):
        word = Word("racecar")
        palindrome = Palindrome(word)
        assert_that(palindrome.is_palindrome(), is_(True))