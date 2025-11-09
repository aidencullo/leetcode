class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_unique = set(banned)
        paragraph = ''.join(c.lower() for c in paragraph)
        words = re.findall(r'\b\w+\b', paragraph)
        counter = Counter(words)
        most_common = ""
        most_common_freq = 0
        for word, freq in counter.items():
            if word not in banned_unique and freq > most_common_freq:
                most_common = word
                most_common_freq = freq
        return most_common
