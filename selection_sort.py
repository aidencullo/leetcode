def selection_sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

def test_selection_sort():
    assert selection_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]
    assert selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

test_selection_sort()
print("All tests passed")pus