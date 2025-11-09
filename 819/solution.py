class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_unique = set(banned)
        paragraph = paragraph.lower()
        words = re.findall(r'\b\w+\b', paragraph)
        words = [word for word in words if word not in banned_unique]
        counter = Counter(words)
        max_word = max(counter.items(), key=lambda x: x[1])[0]
        return max_word
