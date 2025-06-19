class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def is_vowel_substring(start, end):
            return set(word[start: end + 1]) == set("aeiou")

        def is_vowel(index):
            return word[index] in "aeiou"

        def count_vowel_substrings(start, end):
            count = 0
            l, r = start, start
            while r < end + 1:
                while r < end + 1 and not is_vowel_substring(l, r):
                    r += 1
                print(r)
                if r == end + 1:
                    break
                count += 1 + end - r
                l += 1
            return count
            
        
        n = len(word)
        vowel_substrings = 0
        i = 0
        total = 0
        
        while i < n:
            while i < n and not is_vowel(i):
                i += 1
            if i == n:
                break
            start = i
            while i < n and is_vowel(i):
                i += 1
            end = i - 1
            total += count_vowel_substrings(start, end)
        return total
