from functools import cmp_to_key

def compare_ones(a, b):
    return (a % 10) - (b % 10)

def compare_tens(a, b):
    return (a // 10) - (b // 10)

def compare_hundreds(a, b):
    return (a // 100) - (b // 100)



def radixSort(lst):
    lst.sort(key=cmp_to_key(compare_ones))
    lst.sort(key=cmp_to_key(compare_tens))
    lst.sort(key=cmp_to_key(compare_hundreds))
    return lst

arr = [170, 45, 75, 90, 802, 24, 2, 66]
result = radixSort(arr)

output = [2, 24, 45, 66, 75, 90, 170, 802]
assert output == result, f"{result} != {output}"
