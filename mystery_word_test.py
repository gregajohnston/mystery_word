import unittest

from mystery_word import (update_after_guess, select_difficulty,
                          check_duplicate_guess, check_win,
                          exceeds_guess_count)


class TestMysteryWord(unittest.TestCase):

    def test_update_user_correct(self):
        self.assertEqual(update_after_guess('f', 'foo', 4), (True, 4))

    def test_update_user_wrong(self):
        self.assertEqual(update_after_guess('f', 'apple', 4), (False, 5))

    def test_normal_difficulty(self):
        self.assertEqual(select_difficulty('normal'), [6, 8])

    def test_not_hard_difficulty(self):
        self.assertNotEqual(select_difficulty('hard'), [4, 6])

    def test_duplicates(self):
        self.assertTrue(check_duplicate_guess('a', ['a', 'b', 'c']))

    def test_win(self):
        self.assertTrue(check_win('apple', ['a', 'p', 'l', 'e']))

    def test_lose(self):
        self.assertTrue(exceeds_guess_count(8, 8))


if __name__ == '__main__':
    unittest.main()
