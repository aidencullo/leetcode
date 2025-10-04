class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        first_seen = dict()
        minimum_restaurants = []
        import math
        least_index_sum = math.inf
        for i, item in enumerate(list1):
            if item not in first_seen:
                first_seen[item] = i
        for i, item in enumerate(list2):
            if item in first_seen:
                index_sum = i + first_seen[item]
                if index_sum < least_index_sum:
                    least_index_sum = index_sum
                    minimum_restaurants = [item]
                elif index_sum == least_index_sum:
                    minimum_restaurants.append(item)
        return minimum_restaurants

            
