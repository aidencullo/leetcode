class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        last = ""
        longest = ""
        count = 0
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)

        while heap:
            freq, val = heapq.heappop(heap)
            if val == last and count == 2:
                if not heap:
                    break
                next_freq, next_val = heapq.heappop(heap)
                count = 1
                current = next_val
                new_next_freq = next_freq + 1
                if new_next_freq:
                    heapq.heappush(heap, (new_next_freq, next_val))
            else:
                current = val
                count += 1
                new_freq = freq + 1
                if new_freq:
                    heapq.heappush(heap, (new_freq, val))
            longest += current
            last = current
        return longest
