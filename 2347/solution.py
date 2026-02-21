from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        if len(set(ranks)) >= 3:
            return "Three of a Kind"
        if len(set(ranks)) == 2:
            return "Pair"
        return "High Card"
        
