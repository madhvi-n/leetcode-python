class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def bisect_left(height):
            left, right = 0, len(heaters) - 1
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] < height:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        heaters.sort()
        radius = 0
        for house in houses:
            ind = bisect_left(house)
            if ind == len(heaters):
                radius = max(radius, house - heaters[-1])
            elif ind == 0:
                radius = max(radius, heaters[0] - house)
            else:
                radius = max(radius, min(heaters[ind] - house, house - heaters[ind - 1]))
        return radius