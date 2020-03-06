
from variation_builder import get_new_combo, get_new_combos, uniqify_list_of_lists, is_list_not_str, is_list_of_lists, get_new_combos_recursive, is_scalar, convert_to_string
import unittest

class TestIsList(unittest.TestCase):
    def test_is_list_not_str(self):
        self.assertTrue(is_list_not_str([]))
        self.assertFalse(is_list_not_str('asd'))

    def test_is_list_of_lists(self):
        self.assertFalse(is_list_of_lists([]))
        self.assertTrue(is_list_of_lists([['a'], ['b']]))
        self.assertFalse(is_list_of_lists(['a', 'b']))

    def test_is_scalar(self):
        self.assertFalse(is_scalar([]))
        self.assertFalse(is_scalar([['a'], ['b']]))
        self.assertTrue(is_scalar('asd'))

class TestGetCombosRecursive(unittest.TestCase):
    def test_get_new_combos_recursive(self):
        r = get_new_combos_recursive([['Ἰωάννης', 'ό Ἰωάννης'], 'ὰγαπᾷ', 'Μαρίαν'])
        r = sorted(r)

        expected = [
            ['Μαρίαν', 'ό Ἰωάννης', 'ὰγαπᾷ'],
            ['Μαρίαν', 'Ἰωάννης', 'ὰγαπᾷ'],
            ['Μαρίαν', 'ὰγαπᾷ', 'ό Ἰωάννης'],
            ['Μαρίαν', 'ὰγαπᾷ', 'Ἰωάννης'],
            ['ό Ἰωάννης', 'Μαρίαν', 'ὰγαπᾷ'],
            ['ό Ἰωάννης', 'ὰγαπᾷ', 'Μαρίαν'],
            ['Ἰωάννης', 'Μαρίαν', 'ὰγαπᾷ'],
            ['Ἰωάννης', 'ὰγαπᾷ', 'Μαρίαν'],
            ['ὰγαπᾷ', 'Μαρίαν', 'ό Ἰωάννης'],
            ['ὰγαπᾷ', 'Μαρίαν', 'Ἰωάννης'],
            ['ὰγαπᾷ', 'ό Ἰωάννης', 'Μαρίαν'],
            ['ὰγαπᾷ', 'Ἰωάννης', 'Μαρίαν']
        ]

        self.assertEqual(r, expected)

    def test_get_new_combos_wallace(self):
        combinations = [
            ['Ἰωάννης', 'ό Ἰωάννης'],
            'ὰγαπᾷ',
            ['Μαρίαν', 'τὴν Μαρίαν']
        ]
        r = get_new_combos_recursive(combinations)
        r = sorted(r)

        self.assertEqual(len(r), 24)

    def test_get_new_combos_wallace_alt_spellings_john(self):
        combinations = [
            ['Ἰωάννης', 'ό Ἰωάννης', 'Ἰωάνης', 'ό Ἰωάνης'],
            'ὰγαπᾷ',
            ['Μαρίαν', 'τὴν Μαρίαν']
        ]
        r = get_new_combos_recursive(combinations)
        r = sorted(r)

        self.assertEqual(len(r), 48)

    def test_get_new_combos_wallace_alt_spellings_mary(self):
        combinations = [
            ['Ἰωάννης', 'ό Ἰωάννης', 'Ἰωάνης', 'ό Ἰωάνης'],
            'ὰγαπᾷ',
            ['Μαρίαν', 'τὴν Μαρίαν', 'Μαριάμμην', 'τὴν Μαριάμμην']
        ]
        r = get_new_combos_recursive(combinations)
        r = sorted(r)

        self.assertEqual(len(r), 96)

    """
    def test_get_new_combos_recursive_nested(self):
        r = get_new_combos_recursive([['A', ['B', 'B\'']], 'C'])

        r = sorted(r)
        print(r)

        expected = [
            ['A', 'C'],
            ['B', 'C'],
            ["B'", 'C'],
            ['C', 'A'],
            ['C', 'B'],
            ['C', "B'"]
        ]

        self.assertEqual(r, expected)
    """

    def test_get_new_combos_recursive_both_sides(self):
        r = get_new_combos_recursive([['A', 'a'], 'B', ['C', 'c']])

        r = sorted(r)

        expected = [
            ['A', 'B', 'C'],
            ['A', 'B', 'c'],
            ['A', 'C', 'B'],
            ['A', 'c', 'B'],
            ['B', 'A', 'C'],
            ['B', 'A', 'c'],
            ['B', 'C', 'A'],
            ['B', 'C', 'a'],
            ['B', 'a', 'C'],
            ['B', 'a', 'c'],
            ['B', 'c', 'A'],
            ['B', 'c', 'a'],
            ['C', 'A', 'B'],
            ['C', 'B', 'A'],
            ['C', 'B', 'a'],
            ['C', 'a', 'B'],
            ['a', 'B', 'C'],
            ['a', 'B', 'c'],
            ['a', 'C', 'B'],
            ['a', 'c', 'B'],
            ['c', 'A', 'B'],
            ['c', 'B', 'A'],
            ['c', 'B', 'a'],
            ['c', 'a', 'B']
        ]

        self.assertEqual(r, expected)

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
