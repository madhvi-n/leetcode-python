class Solution:
    def trap(self, height: List[int]) -> int:
        
        area = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        
        while left < right:
            if height[left] < height[right]:
                # if height at left is less than right
                # if height at left is greater than left_max, max_left is height at left
                # else update area += left_max - height[left]
                # increase left pointer by 1
                
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    area += left_max - height[left]
                left += 1
            else:
                # check if height at right pointer is greater than right max
                # update right_max if yes or update area += right_max - height[right]
                # decrease right pointer by 1
                
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    area += right_max - height[right]
                right -= 1
        return area