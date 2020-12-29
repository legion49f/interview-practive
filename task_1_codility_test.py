import unittest
from task_1_codility import solution

class TestSolution(unittest.TestCase):
    def test_solution1(self):
        self.assertTrue(solution([1,1,2,3,4,6]) == 5)
    def test_solution2(self):
        self.assertTrue(solution([1,3,6,4,1,2]) == 5)
    def test_solution3(self):
        self.assertTrue(solution([1,2,3]) == 4)
    def test_solution4(self):
        self.assertTrue(solution([-1,-3]) == 1)
    def test_solution5(self):
        self.assertTrue(solution([-1,-2, 0, 11]) == 1)
    def test_solution6(self):
        self.assertTrue(solution([-1,-2, 0, 1, 7]) == 2)
    
    # def test_values(self):
    #     self.assertRaises(ValueError, solution, -2)
    #     self.assertRaises(ValueError, solution, 1.1)
    #     self.assertRaises(ValueError, solution, {1,2,3} )
    #     self.assertRaises(ValueError, solution, [1,2])
    #     self.assertRaises(ValueError, solution, {'car':'mazda', 'house':'apt'} )