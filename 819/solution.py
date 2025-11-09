class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import string
        paragraph = paragraph.lower()
        paragraph = ''.join(map(lambda x: x if x.isalpha() else ' ', paragraph))
        words = paragraph.split()
        words = [word for word in words if word not in banned]
        counter = Counter(words)
        return max(counter, key=counter.get)
