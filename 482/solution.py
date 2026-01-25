class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()
        
        # Calculate size of first group
        first_group = len(s) % k
        
        result = []
        
        # Add first group if it exists
        if first_group:
            result.append(s[:first_group])
        
        # Add remaining groups of size k
        for i in range(first_group, len(s), k):
            result.append(s[i:i+k])
        
        return "-".join(result)
