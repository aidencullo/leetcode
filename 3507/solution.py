class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def remove_pair(arr):
            min_pair = (math.inf, 0, 0)
            n = len(arr)
            for i in range(n - 1):
                pair_sum = arr[i] + arr[i + 1]
                min_pair = min(min_pair, (pair_sum, i, i + 1))

            min_pair_sum, first, _ = min_pair
            new_arr = []
            i = 0
            while i < n:
                if i == first:
                    new_arr.append(min_pair_sum)
                    i += 1
                else:
                    new_arr.append(arr[i])                    
                i += 1
            return new_arr
                    
        steps = 0
        while sorted(nums) != nums:
            print(nums)
            nums = remove_pair(nums)
            steps += 1
        return steps
