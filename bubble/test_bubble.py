import unittest
from bubble import bubble_sort


class TestBubbleSort(unittest.TestCase):
    
    def test_empty_list(self):
        """Test sorting an empty list"""
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])
    
    def test_single_element(self):
        """Test sorting a list with a single element"""
        arr = [5]
        bubble_sort(arr)
        self.assertEqual(arr, [5])
    
    def test_two_elements_sorted(self):
        """Test sorting a list with two elements already sorted"""
        arr = [1, 2]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2])
    
    def test_two_elements_unsorted(self):
        """Test sorting a list with two elements in reverse order"""
        arr = [2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2])
    
    def test_already_sorted(self):
        """Test sorting an already sorted list"""
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a list in reverse order"""
        arr = [5, 4, 3, 2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_random_order(self):
        """Test sorting a list in random order"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicates(self):
        """Test sorting a list with duplicate elements"""
        arr = [5, 2, 8, 2, 5, 1, 8]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 5, 5, 8, 8])
    
    def test_all_same_elements(self):
        """Test sorting a list with all identical elements"""
        arr = [3, 3, 3, 3, 3]
        bubble_sort(arr)
        self.assertEqual(arr, [3, 3, 3, 3, 3])
    
    def test_negative_numbers(self):
        """Test sorting a list with negative numbers"""
        arr = [-5, -2, -8, -1, -3]
        bubble_sort(arr)
        self.assertEqual(arr, [-8, -5, -3, -2, -1])
    
    def test_mixed_positive_negative(self):
        """Test sorting a list with both positive and negative numbers"""
        arr = [5, -2, 0, -5, 3, -1]
        bubble_sort(arr)
        self.assertEqual(arr, [-5, -2, -1, 0, 3, 5])
    
    def test_large_list(self):
        """Test sorting a larger list"""
        arr = list(range(100, 0, -1))
        bubble_sort(arr)
        self.assertEqual(arr, list(range(1, 101)))
    
    def test_floats(self):
        """Test sorting a list of floating point numbers"""
        arr = [3.14, 1.41, 2.71, 0.57, 1.73]
        bubble_sort(arr)
        self.assertEqual(arr, [0.57, 1.41, 1.73, 2.71, 3.14])
    
    def test_strings(self):
        """Test sorting a list of strings"""
        arr = ['banana', 'apple', 'cherry', 'date']
        bubble_sort(arr)
        self.assertEqual(arr, ['apple', 'banana', 'cherry', 'date'])
    
    def test_single_character_strings(self):
        """Test sorting a list of single character strings"""
        arr = ['z', 'a', 'm', 'b']
        bubble_sort(arr)
        self.assertEqual(arr, ['a', 'b', 'm', 'z'])
    
    def test_in_place_modification(self):
        """Test that the function modifies the list in-place"""
        arr = [3, 1, 2]
        original_id = id(arr)
        bubble_sort(arr)
        self.assertEqual(id(arr), original_id)
        self.assertEqual(arr, [1, 2, 3])
    
    def test_very_small_values(self):
        """Test sorting with very small numbers"""
        arr = [0.0001, 0.0003, 0.0002]
        bubble_sort(arr)
        self.assertEqual(arr, [0.0001, 0.0002, 0.0003])
    
    def test_very_large_values(self):
        """Test sorting with very large numbers"""
        arr = [1000000, 500000, 2000000]
        bubble_sort(arr)
        self.assertEqual(arr, [500000, 1000000, 2000000])
    
    def test_alternating_pattern(self):
        """Test sorting a list with alternating high/low pattern"""
        arr = [5, 1, 6, 2, 7, 3, 8, 4]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()

