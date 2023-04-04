class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int)
        
        for index, val in nums1:
            hashmap[index] += val
            
        for index, val in nums2:
            hashmap[index] += val
        
        return sorted(hashmap.items())