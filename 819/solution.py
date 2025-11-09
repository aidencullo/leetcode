class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import string
        for punc in string.punctuation:
            paragraph = paragraph.replace(punc, ' ')
        paragraph = paragraph.lower()
        words = paragraph.split()
        # words = re.findall(r'\b\w+\b', paragraph)
        words = [word for word in words if word not in banned and word]
        counter = Counter(words)
        return max(counter, key=counter.get)
