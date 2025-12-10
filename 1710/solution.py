class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=itemgetter(1), reverse=True)
        units = 0
        i = 0
        n = len(boxTypes)
        while truckSize > 0 and i < n:
            if boxTypes[i][0] == 0:
                i += 1
                continue
            units += boxTypes[i][1]
            boxTypes[i][0] -= 1
            truckSize -= 1
        return units

