class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)
        diff = (b - a) // 2
        bobSizesSet = set(bobSizes)
        for size in aliceSizes:
            if size + diff in bobSizesSet:
                return [size, size + diff]
