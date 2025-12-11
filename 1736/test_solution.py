import unittest
from solution import Solution

class TestMaximumTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_all_question_marks(self):
        result = self.solution.maximumTime("??:??")
        self.assertEqual(result, "23:59")
    
    def test_no_question_marks(self):
        result = self.solution.maximumTime("23:59")
        self.assertEqual(result, "23:59")
    
    def test_hour_first_digit_question_mark(self):
        result = self.solution.maximumTime("?3:00")
        self.assertEqual(result, "23:00")
    
    def test_hour_second_digit_question_mark(self):
        result = self.solution.maximumTime("2?:00")
        self.assertEqual(result, "23:00")
    
    def test_hour_first_digit_question_mark_with_high_second_digit(self):
        result = self.solution.maximumTime("?9:00")
        self.assertEqual(result, "19:00")
    
    def test_minute_question_marks(self):
        result = self.solution.maximumTime("12:??")
        self.assertEqual(result, "12:59")
    
    def test_mixed_question_marks(self):
        result = self.solution.maximumTime("?4:5?")
        self.assertEqual(result, "14:59")
    
    def test_edge_case_00_00(self):
        result = self.solution.maximumTime("00:00")
        self.assertEqual(result, "00:00")
    
    def test_edge_case_23_59(self):
        result = self.solution.maximumTime("23:59")
        self.assertEqual(result, "23:59")
    
    def test_hour_both_question_marks(self):
        result = self.solution.maximumTime("??:30")
        self.assertEqual(result, "23:30")
    
    def test_minute_first_digit_question_mark(self):
        result = self.solution.maximumTime("15:?9")
        self.assertEqual(result, "15:59")
    
    def test_minute_second_digit_question_mark(self):
        result = self.solution.maximumTime("15:5?")
        self.assertEqual(result, "15:59")

if __name__ == '__main__':
    unittest.main()

