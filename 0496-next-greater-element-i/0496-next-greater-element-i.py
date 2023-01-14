class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1_index = {num: index for index, num in enumerate(nums1)}
#         res = [-1] * len(nums1)
#         stack = []

#         for i in range(len(nums2)):
#             cur = nums2[i]
#             while stack and cur > stack[-1]:
#                 val = stack.pop()
#                 idx = nums1_index[val]
#                 res[idx] = cur
#             if cur in nums1_index:
#                 stack.append(cur)
#         return res
    
        stack = []
        hashmap = dict()
        
        for i in range(len(nums2)):
            hashmap[nums2[i]] = -1
            
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                curr = stack.pop()
                hashmap[curr] = nums2[i]
                
            stack.append(nums2[i])
            
        for i in range(len(nums1)):
            nums1[i] = hashmap[nums1[i]]
        
        return nums1