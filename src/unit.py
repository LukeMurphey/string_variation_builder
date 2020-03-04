
from variation_builder import get_new_combo, get_new_combos, uniqify_list_of_lists
import unittest

class TestGetNewCombos(unittest.TestCase):
    def test_get_new_combos_greek(self):
        r = get_new_combos(['Ἰωάννης', 'ό Ἰωάννης'], [['ὰγαπᾷ', 'Μαρίαν']])
        r = sorted(r)

        expected = [
            ['ό Ἰωάννης', 'ὰγαπᾷ', 'Μαρίαν'],
            ['Ἰωάννης', 'ὰγαπᾷ', 'Μαρίαν'],
            ['ὰγαπᾷ', 'Μαρίαν', 'ό Ἰωάννης'],
            ['ὰγαπᾷ', 'Μαρίαν', 'Ἰωάννης'],
            ['ὰγαπᾷ', 'ό Ἰωάννης', 'Μαρίαν'],
            ['ὰγαπᾷ', 'Ἰωάννης', 'Μαρίαν']
        ]

        self.assertEqual(r, expected)

    def test_get_new_combos_greek2(self):
        r = get_new_combos(['Ἰωάννης', 'ό Ἰωάννης'], [['ὰγαπᾷ', 'Μαρίαν']])
        r = sorted(r)

        expected = [
            ['ό Ἰωάννης', 'ὰγαπᾷ', 'Μαρίαν'],
            ['Ἰωάννης', 'ὰγαπᾷ', 'Μαρίαν'],
            ['ὰγαπᾷ', 'Μαρίαν', 'ό Ἰωάννης'],
            ['ὰγαπᾷ', 'Μαρίαν', 'Ἰωάννης'],
            ['ὰγαπᾷ', 'ό Ἰωάννης', 'Μαρίαν'],
            ['ὰγαπᾷ', 'Ἰωάννης', 'Μαρίαν']
        ]

        self.assertEqual(r, expected)

    def test_get_new_combos_simple2(self):
        r = get_new_combos(['a', 'b'])
        r = sorted(r)

        self.assertEqual(r, [['a'], ['b']])

    def test_get_new_combos(self):
        r = get_new_combos(['a', 'b'], [['c']])
        r = sorted(r)

        self.assertEqual(r, [['a', 'c'], ['b', 'c'], ['c', 'a'], ['c', 'b']])

class TestGetNewCombo(unittest.TestCase):
    def test_get_new_combo(self):
        r = get_new_combo(['ὰγαπᾷ'], 'Μαρίαν')
        r = sorted(r)

        # self.assertEqual(r, [['Μαρίαν', 'ὰγαπᾷ'], ['ὰγαπᾷ', 'Μαρίαν']])

    def test_get_new_combo2(self):
        r = get_new_combo(['a', 'b'], 'c')
        r = sorted(r)

        self.assertEqual(r, [['a', 'b', 'c'], ['a', 'c', 'b'], ['c', 'a', 'b']])

    def test_get_new_combo_dupes(self):
        r = get_new_combo(['ὰγαπᾷ', 'Μαρίαν'], 'Μαρίαν')
        r = sorted(r)

        self.assertEqual(len(r), 2)
        self.assertEqual(r, [['Μαρίαν', 'ὰγαπᾷ', 'Μαρίαν'], ['ὰγαπᾷ', 'Μαρίαν', 'Μαρίαν']])

class TestUniqueness(unittest.TestCase):
    def test_remove_dupes(self):
        l = ["a", "b", "c"], ["a", "b", "c"], ["b", "a", "c"]

        result = uniqify_list_of_lists(l)
        result = sorted(result)

        self.assertEqual(result, [['a', 'b', 'c'], ['b', 'a', 'c']])

if __name__ == '__main__':
    unittest.main()
