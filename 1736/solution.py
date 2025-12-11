class Solution:
    def maximumTime(self, t: str) -> str:
        h1_orig, h2_orig, _, m1_orig, m2_orig = t
        
        h1_computed = '2' if h1_orig == '?' and (h2_orig == '?' or h2_orig <= '3') else ('1' if h1_orig == '?' else h1_orig)
        h2_computed = '3' if h2_orig == '?' and h1_computed == '2' else ('9' if h2_orig == '?' else h2_orig)
        m1_computed = '5' if m1_orig == '?' else m1_orig
        m2_computed = '9' if m2_orig == '?' else m2_orig
        
        return f"{h1_computed}{h2_computed}:{m1_computed}{m2_computed}"
