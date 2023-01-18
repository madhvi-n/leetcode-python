class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = dict(Counter(arr))
        res = [key for key, val in hashmap.items() if val == 1]
        return res[k - 1] if len(res) >= k else ""
        
            
        