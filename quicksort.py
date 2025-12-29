def quicksort(arr):
    """
    Implement quicksort algorithm to sort an array in ascending order.

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Algorithm steps:
    1. Base case: arrays with 0 or 1 element are already sorted
    2. Choose a pivot element (commonly the last element)
    3. Partition: rearrange elements so that:
       - Elements less than pivot are on the left
       - Elements greater than pivot are on the right
    4. Recursively sort the left and right partitions
    5. Combine the results
    """
    # TODO: Implement quicksort here
    pass


# ============================================================================
# TESTS
# ============================================================================

def test_quicksort():
    """Run all quicksort tests"""

    # Test 1: Empty array
    assert quicksort([]) == [], "Failed: empty array"
    print("✓ Test 1 passed: empty array")

    # Test 2: Single element
    assert quicksort([5]) == [5], "Failed: single element"
    print("✓ Test 2 passed: single element")

    # Test 3: Two elements - sorted
    assert quicksort([1, 2]) == [1, 2], "Failed: two elements already sorted"
    print("✓ Test 3 passed: two elements already sorted")

    # Test 4: Two elements - unsorted
    assert quicksort([2, 1]) == [1, 2], "Failed: two elements unsorted"
    print("✓ Test 4 passed: two elements unsorted")

    # Test 5: Already sorted array
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Failed: already sorted"
    print("✓ Test 5 passed: already sorted array")

    # Test 6: Reverse sorted array
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Failed: reverse sorted"
    print("✓ Test 6 passed: reverse sorted array")

    # Test 7: Random array
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9], "Failed: random array"
    print("✓ Test 7 passed: random array")

    # Test 8: Array with duplicates
    assert quicksort([4, 2, 4, 2, 4, 2]) == [2, 2, 2, 4, 4, 4], "Failed: duplicates"
    print("✓ Test 8 passed: array with duplicates")

    # Test 9: All same elements
    assert quicksort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7], "Failed: all same elements"
    print("✓ Test 9 passed: all same elements")

    # Test 10: Negative numbers
    assert quicksort([-5, -1, -3, -2, -4]) == [-5, -4, -3, -2, -1], "Failed: negative numbers"
    print("✓ Test 10 passed: negative numbers")

    # Test 11: Mixed positive and negative
    assert quicksort([3, -1, 4, -5, 2, 0, -2]) == [-5, -2, -1, 0, 2, 3, 4], "Failed: mixed pos/neg"
    print("✓ Test 11 passed: mixed positive and negative")

    # Test 12: Large array with random values
    large_unsorted = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 18, 77, 55]
    large_sorted = [11, 12, 18, 22, 23, 25, 34, 36, 45, 50, 55, 64, 77, 88, 90]
    assert quicksort(large_unsorted) == large_sorted, "Failed: large array"
    print("✓ Test 12 passed: large array")

    # Test 13: Array with many duplicates
    assert quicksort([5, 2, 8, 2, 9, 1, 5, 5]) == [1, 2, 2, 5, 5, 5, 8, 9], "Failed: many duplicates"
    print("✓ Test 13 passed: many duplicates")

    # Test 14: Three elements in reverse
    assert quicksort([3, 2, 1]) == [1, 2, 3], "Failed: three elements reverse"
    print("✓ Test 14 passed: three elements in reverse")

    # Test 15: Large range of values
    assert quicksort([100, -100, 50, -50, 0, 75, -75]) == [-100, -75, -50, 0, 50, 75, 100], "Failed: large range"
    print("✓ Test 15 passed: large range of values")

    # Test 16: Stress test - larger array
    import random
    random.seed(42)
    stress_test = [random.randint(-100, 100) for _ in range(100)]
    result = quicksort(stress_test[:])  # Copy to avoid mutation
    expected = sorted(stress_test)
    assert result == expected, "Failed: stress test with 100 elements"
    print("✓ Test 16 passed: stress test with 100 elements")

    # Test 17: Check that original array is not mutated (if using copy)
    original = [3, 1, 4, 1, 5]
    result = quicksort(original)
    # This test depends on implementation - comment out if you modify in place
    # assert original == [3, 1, 4, 1, 5], "Failed: original array was mutated"
    # print("✓ Test 17 passed: original array not mutated")

    print("\n" + "="*50)
    print("All tests passed! ✓")
    print("="*50)


if __name__ == "__main__":
    test_quicksort()
