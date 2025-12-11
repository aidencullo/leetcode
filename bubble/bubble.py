def bubble_sort(arr):
    n = len(arr)
    for end in range(n - 1, -1, -1):
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
            
        
