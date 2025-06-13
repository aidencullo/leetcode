class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = 3 * code
        decrypted = []
        if k > 0:
            for i in range(n, 2 * n):
                decrypted.append(sum(code[i + 1: i + 4]))
        if k < 0:
            for i in range(n, 2 * n):
                decrypted.append(sum(code[i - 3: i])) 
        if k == 0:
            for i in range(n, 2 * n):
                decrypted.append(0)                   
        return decrypted
