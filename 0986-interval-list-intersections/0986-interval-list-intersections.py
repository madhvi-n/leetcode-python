class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # Let's check if firstList[i] intersects secondList[j].
            # low - the startpoint of the intersection
            # high - the endpoint of the intersection
            
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            
            if low <= high:
                ans.append([low, high])

            # Remove the interval with the smallest endpoint
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans
        
        