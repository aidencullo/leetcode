class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from itertools import permutations
        perms = [''.join(p) for p in permutations(words)]
        perms = set(perms)

        return [i for i in range(len(s)) if s[i: i + len(perms[0])] in perms]
