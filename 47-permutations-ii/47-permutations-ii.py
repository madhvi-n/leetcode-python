class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        count = {n: 0 for n in nums}
        
        # hashmap of nums with count
        for num in nums:
            count[num] += 1
            
        
        def dfs():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            
            for num in count.keys():
                if count[num] > 0:
                    permutation.append(num)
                    count[num] -= 1 
                    
                    dfs()
                    
                    count[num] += 1
                    permutation.pop()
        dfs()
        return result