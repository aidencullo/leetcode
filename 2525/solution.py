class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = max(length, width, height, mass) >= 10 ** 4 or length * height * width >= 10 ** 9
        is_heavy = mass >= 100
        if is_heavy and is_bulky:
            return "Both"
        if not is_heavy and not is_bulky:
            return "Neither"
        if is_heavy:
            return "Heavy"
        return "Bulky"
