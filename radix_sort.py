from functools import cmp_to_key

def get_place(n):
    def get(a):
        m = n
        while m > 0:
            a //= 10
            m -= 1
        return a % 10
    return get

def compare_custom(n):
    get = get_place(n)
    def cmp(a, b):
        return get(a) - get(b)
    return cmp

def compare_ones(a, b):
    cmp = compare_custom(0)
    return cmp(a, b)

def compare_tens(a, b):
    cmp = compare_custom(1)
    return cmp(a, b)

def compare_hundreds(a, b):
    cmp = compare_custom(2)
    return cmp(a, b)

def radixSort(lst):
    lst.sort(key=cmp_to_key(compare_ones))
    lst.sort(key=cmp_to_key(compare_tens))
    lst.sort(key=cmp_to_key(compare_hundreds))
    return lst

arr = [170, 45, 75, 90, 802, 24, 2, 66]
result = radixSort(arr)

output = [2, 24, 45, 66, 75, 90, 170, 802]
assert output == result, f"{result} != {output}"
