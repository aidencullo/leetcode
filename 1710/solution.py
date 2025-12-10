BOX_COUNT_INDEX = 0

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def maximize(remaining_box_slots, loaded_units):
            nonlocal maximum_units
            if remaining_box_slots < 0:
                return
            maximum_units = max(maximum_units, loaded_units)

            for i, (box_count, current_box_units) in enumerate(boxTypes):
                if box_count == 0:
                    continue
                boxTypes[i][BOX_COUNT_INDEX] -= 1
                maximize(remaining_box_slots - 1, loaded_units + current_box_units)
                boxTypes[i][BOX_COUNT_INDEX] += 1

        maximum_units = -math.inf
        initial_units_loaded = 0
        maximize(truckSize, initial_units_loaded)
        return maximum_units
