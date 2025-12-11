class Solution:
    def maximumTime(self, t: str) -> str:
        h1, h2, _, m1, m2 = t
        h1 = '2' if h1 == '?' and (h2 == '?' or h2 <= '3') else ('1' if h1 == '?' else h1)
        h2 = '3' if h2 == '?' and h1 == '2' else ('9' if h2 == '?' else h2)
        m1 = '5' if m1 == '?' else m1
        m2 = '9' if m2 == '?' else m2
        return f"{h1}{h2}:{m1}{m2}"
