class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def process(idx, word):
            res = ""
            char = word[0]
            is_vowel = char.lower() in "aeiou"
            if is_vowel:
                res = word
            else:
                res = word[1:] + char
            res += "ma"
            res += 'a' * (idx + 1)
            return res
        
        return ' '.join([process(i, word) for i, word in enumerate(sentence.split())])
