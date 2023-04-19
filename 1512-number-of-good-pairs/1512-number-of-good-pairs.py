class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and i < j:
        #             count += 1
        # return count
        
        # number of good pairs
        repeat = {}
        pairs = 0
        
        # for every element in nums
        for val in nums:
            
            # number of repeated digits
            if val in repeat:
                
                # count number of pairs based on duplicate values
                if repeat[val] == 1:
                    pairs += 1
                else:
                    pairs += repeat[val]
                
                # increment the number of counts
                repeat[val] += 1
                
            # number has not been seen before
            else:
                repeat[val] = 1
        
        return pairs
        
        