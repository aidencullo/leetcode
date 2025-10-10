class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        def get_element(i):
            return colors[i % n]

        alternating_groups = 0
        n = len(colors)
        for i in range(n):
            left = get_element(i)
            middle = get_element(i + 1)
            right = get_element(i + 2)
            if left != middle and middle != right:
                alternating_groups += 1
        return alternating_groups
