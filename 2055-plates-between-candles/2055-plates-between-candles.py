class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]
        candles = []

        for i, char in enumerate(s): 
            if char == '|': 
                candles.append(i)
                
            if char == '|': 
                prefix.append(prefix[-1])
            else: 
                prefix.append(prefix[-1] + 1)
        
        ans = []
        for x, y in queries: 
            low = bisect_left(candles, x)
            high = bisect_right(candles, y) - 1
            
            if 0 <= high and low < len(candles) and low <= high: 
                ans.append(prefix[candles[high]+1] - prefix[candles[low]])
            else: 
                ans.append(0)
        return ans