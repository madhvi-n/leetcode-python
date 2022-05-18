class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        
        result = []
        
        for key, count in counter.items():
            if key == count:
                result.append(key)
        
        return max(result) if result else -1