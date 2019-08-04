import unittest
from prefix_tree import Trie

class TireTest(unittest.TestCase):
    """
    functionality test
    """
    def test_empty_string(self):
        trie = Trie()
        trie.insert('')
        self.assertFalse(trie.query(''))
        self.assertEqual(trie.startWith(''), 0)
        self.assertEqual(trie.listAllMatches(''), [])

    def test_single_string_query(self):
        trie =  Trie()
        trie.insert('abcd')
        self.assertTrue(trie.query('abcd'))
        self.assertFalse(trie.query('abc'))
        self.assertFalse(trie.query('abcde'))
        self.assertFalse(trie.query(''))
        self.assertFalse(trie.query('axcd'))
        self.assertFalse(trie.query('trie'))

    def test_multi_string_query(self):
        trie = Trie()
        trie.insert('abcd')
        self.assertTrue(trie.query('abcd'))
        self.assertFalse(trie.query('abc'))
        self.assertFalse(trie.query('abcde'))
        trie.insert('axcd')
        self.assertTrue(trie.query('abcd'))
        self.assertTrue(trie.query('axcd'))
        self.assertFalse(trie.query('ax'))

    def test_list_all_matches(self):
        trie = Trie()
        trie.insert('abcd')
        trie.insert('abop')
        trie.insert('ab12')
        trie.insert('abcx')
        self.assertEqual(len(trie.listAllMatches('ab')), 4)
        self.assertEqual(sorted(trie.listAllMatches('ab')), sorted(['abcd', 'abop', 'ab12', 'abcx']))
        self.assertEqual(len(trie.listAllMatches('abc')), 2)
        self.assertEqual(sorted(trie.listAllMatches('abc')), sorted(['abcd', 'abcx']))
        self.assertEqual(trie.listAllMatches('ab1'), ['ab12'])
        self.assertEqual(len(trie.listAllMatches('abcd1')), 0)

    def test_delete(self):
        trie = Trie()
        trie.insert('abcd')
        trie.insert('axcd')
        self.assertTrue(trie.query('abcd'))
        self.assertTrue(trie.query('axcd'))
        self.assertFalse(trie.lazyDelete('abc'))
        self.assertFalse(trie.lazyDelete('abcd1'))
        self.assertTrue(trie.lazyDelete('abcd'))
        self.assertFalse(trie.query('abcd'))
        self.assertTrue(trie.query('axcd'))
        self.assertFalse(trie.lazyDelete(''))
