from unittest import TestCase
from lib.word import Word


class TestWord(TestCase):

    def setUp(self):
        self.word = Word("noon")

    def test_first_is_equal(self):
        self.assertEquals("n", self.word.letter_at(0))

    def test_get_last_index(self):
        self.assertEquals(3, self.word.last_index())

    def test_second_letter_equal(self):
        self.assertEquals("o", self.word.letter_at(1))

    def test_third_letter_is_equal(self):
        self.assertEquals("o", self.word.letter_at(2))

    def test_not_equal(self):
        self.assertNotEqual("o", self.word.letter_at(3))

    def test_return_word_length(self):
        self.assertEquals(4, self.word.length())

    def test_returns_word_length_given_longer_word(self):
        word = Word("spontaneous")
        self.assertEquals(11, word.length())