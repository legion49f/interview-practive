import unittest
from task_1_codility import solution

class TestFindIndex(unittest.TestCase):
    def test_solution(self):
        self.assertTrue(solution([1,1,2,3,4,6]) == 5)
        self.assertTrue(solution([1,3,6,4,1,2]) == 5)
        self.assertTrue(solution([1,2,3]) == 4)
        self.assertTrue(solution([-1,-3]) == 1)
    
    # def test_values(self):
    #     self.assertRaises(ValueError, solution, -2)
    #     self.assertRaises(ValueError, solution, 1.1)
    #     self.assertRaises(ValueError, solution, {1,2,3} )
    #     self.assertRaises(ValueError, solution, [1,2])
    #     self.assertRaises(ValueError, solution, {'car':'mazda', 'house':'apt'} )