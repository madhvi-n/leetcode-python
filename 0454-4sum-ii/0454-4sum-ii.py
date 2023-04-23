class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        num_dict = {}
        
        for i in nums3:
            for j in nums4:
                s = i + j
                if s in num_dict:
                    num_dict[s] += 1
                else:
                    num_dict[s] = 1

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                target = 0 - (nums1[i] + nums2[j])
                if target in num_dict:
                    count += num_dict[target]
        return count    