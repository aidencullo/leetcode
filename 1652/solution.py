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
            initial_sum = circular_sum(0, k)
            running_sum = initial_sum
            for i in range(n):
                running_sum -= code[i % n]
                running_sum += code[(i + k) % n]
                decrypted.append(running_sum)
        if k < 0:
            initial_sum = circular_sum(k - 1, -1)
            running_sum = initial_sum
            for i in range(n):
                running_sum += code[(i - 1) % n]
                running_sum -= code[(i + k - 1) % n]
                decrypted.append(running_sum)
        if k == 0:
            for i in range(n):
                decrypted.append(0)                   
        return decrypted
