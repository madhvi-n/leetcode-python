class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for j in range(len(nums1)):
            j_max = nums1[j]
            for i in range(nums2.index(j_max), len(nums2)):
                if nums2[i] > nums1[j]:
                    j_max = nums2[i]
                    break
                else:
                    continue
            if j_max == nums1[j]:
                res.append(-1)
            else:
                res.append(j_max)
        
        return res