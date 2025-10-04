class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) < len(list2):
            shorter_list = list1
            longer_list = list2
        else:
            shorter_list = list2
            longer_list = list1
            
        first_seen = dict()
        minimum_restaurants = []
        import math
        least_index_sum = math.inf
        for i, restaurant in enumerate(shorter_list):
            if restaurant not in first_seen:
                first_seen[restaurant] = i
        for i, restaurant in enumerate(longer_list):
            if restaurant in first_seen:
                index_sum = i + first_seen[restaurant]
                if index_sum < least_index_sum:
                    least_index_sum = index_sum
                    minimum_restaurants = [restaurant]
                elif index_sum == least_index_sum:
                    minimum_restaurants.append(restaurant)
        return minimum_restaurants

            
