class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         if n == 1:
#             return 1
        
#         result = 2
        
#         for i in range(n):
#             hashmap = collections.defaultdict(int)
#             for j in range(n):
#                 if j != i:
#                     hashmap[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
#             result = max(result, max(hashmap.values()) + 1)
#         return result

        def calc_slope(x1, x2, y1, y2):
            return ((y2 - y1) / (x2 - x1)) if x1 != x2 else float("inf")

        result = 1
        for index1 in range(len(points)):
            slopes = Counter()
            max_points = 1
            x1, y1 = points[index1]
            for index2 in range(index1 + 1, len(points)):
                x2, y2 = points[index2]
                slope = calc_slope(x1, x2, y1, y2)
                slopes[slope] += 1
                max_points = max(max_points, 1 + slopes[slope])
            result = max(result, max_points)
        return result