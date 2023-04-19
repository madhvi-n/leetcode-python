class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        trie = dict()
        
        n = len(nums)
        ans = 0
        for start in range(n):
            count = 0
            cur = trie
            
            for j in range(start, n):
                num = nums[j]
                
                if num % p == 0:
                    count += 1
                    
                if count > k:
                    break
                
                if num not in cur:
                    cur[num] = dict()
                    ans += 1
                cur = cur[num]
                    
        return ans 









