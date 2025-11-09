class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_unique = set(banned)
        paragraph = ''.join(c.lower() for c in paragraph)
        words = re.findall(r'\b\w+\b', paragraph)
        counter = Counter(words)
        most_common = ""
        most_common_freq = 0
        word_counts = [(k, v) for k, v in counter.items() if k not in banned]
        max_word = max(word_counts, key=lambda x: x[1])[0]
        return max_word
