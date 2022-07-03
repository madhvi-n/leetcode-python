class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()
        
        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1
        
        
        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            
            res = 0
            if not overlap(charSet, arr[i]):
                for char in arr[i]:
                    charSet.add(char)
                res = backtrack(i + 1)
                for char in arr[i]:
                    charSet.remove(char)
            return max(res, backtrack(i + 1))
        
        return backtrack(0)