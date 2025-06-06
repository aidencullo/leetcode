class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while 1:
            element = tickets.pop(0)
            element -= 1
            time += 1
            k -= 1

            if element == 0 and k == -1:
                break
            if element != 0 and k == -1:
                tickets.append(element)
                k = len(tickets) - 1
                continue
            if element == 0 and k != -1:
                continue
            if element != 0 and k != -1:
                tickets.append(element)
                continue

        return time            
