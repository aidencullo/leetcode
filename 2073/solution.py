class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        total = 0
        n = len(tickets)
        
        for i in range(k + 1):
            total += min(tickets[i], target)
        for i in range(k + 1, n):
            total += min(tickets[i], target - 1)
        return total
