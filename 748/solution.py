from collections import Counter


def lower_char(char):
    ascii_value = ord(char)
    if ascii_value > 64 and ascii_value < 91:
        ascii_value += 32
    return chr(ascii_value)


def lower_word(word):
    lowered_chars = list(map(lower_char, word))
    return ''.join(lowered_chars)


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:

        def remove_non_letters(word):
            lowercase_word = lower_word(word)
            only_letters = [c for c in lowercase_word if c.isalpha()]
            return only_letters

        def is_subset(a, b):
            return not (a - b)

        licensePlate_letters = remove_non_letters(licensePlate)
        licensePlate_counter = Counter(licensePlate_letters)
        shortest = math.inf
        res = []
        for word in words:
            word_counter = Counter(word)
            if is_subset(licensePlate_counter, word_counter):
                res.append(word)

        return min(res, key=len)


def test_lower_char():
    import string

    for c in string.ascii_letters:
        print("testing {}".format(c))
        assert lower_char(c) == c.lower()


test_lower_char()
