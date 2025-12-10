class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=itemgetter(1), reverse=True)
        units = 0
        i = 0
        n = len(boxTypes)
        truck_box_slots = truckSize
        while truck_box_slots > 0 and i < n:
            box_type_units = boxTypes[i][1]
            box_type_boxes = boxTypes[i][0]
            possible_boxes_to_add = min(box_type_boxes, truck_box_slots)
            units += possible_boxes_to_add * box_type_units
            boxTypes[i][0] -= possible_boxes_to_add
            truck_box_slots -= possible_boxes_to_add
            i += 1
        return units

