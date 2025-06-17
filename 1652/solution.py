class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def circular_sum(start, end):
            total = 0
            for i in range(start, end):
                total += code[i % len(code)]
            return total

        n = len(code)
        decrypted = []
        if k > 0:
            for i in range(n):
                decrypted.append(circular_sum(i + 1, i + 1 + k))
        if k < 0:
            for i in range(n):
                decrypted.append(circular_sum(i + k, i))
        if k == 0:
            for i in range(n):
                decrypted.append(0)                   
        return decrypted
