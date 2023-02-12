class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        freq = dict()
        maxlen = 0
        for num in nums:
            if num % 2 == 0:
                freq[num] = 1 + freq.get(num, 0)
                maxlen = max(maxlen, freq.get(num))
        
        if len(freq) == 0:
            return -1
        
        stack = []
        for key, val in freq.items():
            if val == maxlen:
                while stack and key < stack[-1]:
                    stack.pop()
                stack.append(key)
            print(stack)
        return stack[0]