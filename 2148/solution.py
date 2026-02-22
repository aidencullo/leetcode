def countElements(nums: List[int]) -> int:
    return sum(min(nums) < x < max(nums) for x in nums)
