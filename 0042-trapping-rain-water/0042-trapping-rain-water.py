class Solution:
    def trap(self, height: List[int]) -> int:
#         ans = 0
        
#         n = len(height)
        
#         for i in range(n):
#             left_max, right_max = 0, 0
            
#             # Find max height to the left of index i
#             for j in range(i, -1, -1):
#                 left_max = max(left_max, height[j])
            
#             # Find max height to the right of index i
#             for j in range(i, n):
#                 right_max = max(right_max, height[j])
            
#             ans += min(left_max, right_max) - height[i]
        
#         return ans

        areas = 0
        leftMax = rightMax = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    areas += leftMax - height[left]
                left +=1
                
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    areas += rightMax - height[right]
                right -=1
        return areas