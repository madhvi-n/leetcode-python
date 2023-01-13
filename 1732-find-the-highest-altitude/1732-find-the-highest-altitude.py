class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0] * (len(gain) + 1)
        
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            altitudes[i + 1] = curr
        
        return max(altitudes)