class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Keep track of frequency of even numbers and max frequency 
        freq = dict()
        maxlen = 0
        for num in nums:
            if num % 2 == 0:
                freq[num] = 1 + freq.get(num, 0)
                maxlen = max(maxlen, freq.get(num))
        
        # if dict is empty, return -1 since all numbers are odd
        if len(freq) == 0:
            return -1
        
        # Iterate through frequency
        # Push the key if values equals maxlen
        # Create a monotonic stack in ascending order
        
        stack = []
        for key, val in freq.items():
            if val == maxlen:
                while stack and key < stack[-1]:
                    stack.pop()
                stack.append(key)
        return stack[0]