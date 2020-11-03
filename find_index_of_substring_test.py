import unittest
from find_index_of_substring import find_index

class TestFindIndex(unittest.TestCase):
    def test_find_index(self):
        self.assertTrue(find_index('pablo echegorri', 'eche') == 6)
        self.assertTrue(find_index('pablo echegorri' , 'p') == 0)
        self.assertTrue(find_index('pablo echegorri' , 'i') == 14)
        self.assertTrue(find_index('pablo echegorri' , 'echo') == -1)
        self.assertTrue(find_index('echo' , 'pablo echegorri') == -1)
    
    def test_values(self):
        self.assertRaises(ValueError, find_index, -2)
        self.assertRaises(ValueError, find_index, 1.1)
        self.assertRaises(ValueError, find_index, {1,2,3} )
        self.assertRaises(ValueError, find_index, [1,2])
        self.assertRaises(ValueError, find_index, {'car':'mazda', 'house':'apt'} )