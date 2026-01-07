class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        last = ""
        longest = 0
        count = 0
        heap = [(a, 'a'), (b, 'b'), (c, 'c')]
        heapq.heapify(heap)

        while heap:
            freq, val = heapq.heappop(heap)
            if val == last and count == 2:
                if not heap:
                    break
                next_freq, next_val = heapq.heappop(heap)
                count = 1
                last = next_val
                if next_freq:
                    heapq.heappush(heap, (next_freq - 1, next_val))
            else:
                last = val
                count += 1
            if freq:
                heapq.heappush(heap, (freq - 1, val))
            longest += 1
        return longest
