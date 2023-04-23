class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hashmap = dict()
        
        for i in nums3:
            for j in nums4:
                s = i + j
                if s in hashmap:
                    hashmap[s] += 1
                else:
                    hashmap[s] = 1

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                target = 0 - (nums1[i] + nums2[j])
                if target in hashmap:
                    count += hashmap[target]
        return count    