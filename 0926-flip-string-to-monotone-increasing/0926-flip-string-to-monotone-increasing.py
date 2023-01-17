class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroCount = 0
        
        # count no of 0's and 1's
        for bit in s:
            if bit == '0':
                zeroCount += 1
        
        # initialize answer with no of 0's since flipping 0's can give you monotonic increasing string
        ans = zeroCount
        
        # Scan the input string. For each 0 bit, decrease count of zero by 1 and replace ans with m if m is smaller
        # For each character increase m by 1
        for bit in s:
            if bit == '0':
                zeroCount -= 1
                ans = min(ans, zeroCount)
            else:
                zeroCount += 1
        return ans