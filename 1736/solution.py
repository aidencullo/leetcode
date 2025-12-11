class Solution:
    def maximumTime(self, t: str) -> str:
        h1_orig, h2_orig, _, m1_orig, m2_orig = t
        
        h1_computed = h1_orig
        if h1_orig == '?' and h2_orig == '?':
            h1_computed = '2'
        if h1_orig == '?' and h2_orig != '?' and h2_orig <= '3':
            h1_computed = '2'
        if h1_orig == '?' and h2_orig != '?' and h2_orig > '3':
            h1_computed = '1'
        
        h2_computed = h2_orig
        if h2_orig == '?' and h1_computed == '2':
            h2_computed = '3'
        if h2_orig == '?' and h1_computed != '2':
            h2_computed = '9'
        
        m1_computed = m1_orig
        if m1_orig == '?':
            m1_computed = '5'
        
        m2_computed = m2_orig
        if m2_orig == '?':
            m2_computed = '9'
        
        return f"{h1_computed}{h2_computed}:{m1_computed}{m2_computed}"
