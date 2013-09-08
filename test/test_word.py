from unittest import TestCase
from lib.word import Word
from hamcrest import *


class TestWord(TestCase):

    def setUp(self):
        self.word = Word("noon")

    def test_first_is_equal(self):
        assert_that(self.word.letter_at(0), is_("n"))

    def test_get_last_index(self):
        assert_that(self.word.last_index(), is_(3))

    def test_second_letter_equal(self):
        assert_that(self.word.letter_at(1), is_("o"))

    def test_third_letter_is_equal(self):
        assert_that(self.word.letter_at(2), is_("o"))

    def test_not_equal(self):
        assert_that(self.word.letter_at(3), is_not("o"))

    def test_return_word_length(self):
        assert_that(self.word.length(), is_(4))

    def test_returns_word_length_given_longer_word(self):
        word = Word("spontaneous")
        assert_that(word.length(), is_(11))