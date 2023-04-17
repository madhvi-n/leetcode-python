class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        hashmap = dict(Counter(nums))
        
        for key, val in hashmap.items():
            if key > 0:
                pos += val
            elif key < 0:
                neg += val
        return max(pos, neg)