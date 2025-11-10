class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash_register = defaultdict(int)
        for bill in bills:
            if bill == 5:
                cash_register[bill] += 1
                continue
            elif bill == 10:
                if 5 not in cash_register:
                    return False
                cash_register[5] -= 1
                cash_register[10] += 1
            else: 
                if cash_register[5] >= 1 and cash_register[10] >= 1:
                    cash_register[5] -= 1
                    cash_register[10] -= 1
                    # cash_register[20] += 1
                    continue
                if cash_register[5] >= 3:
                    cash_register[5] -= 3
                    continue
                return False
        return True
            
