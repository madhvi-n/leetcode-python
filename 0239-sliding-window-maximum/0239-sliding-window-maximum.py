class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Initialize an empty deque q to store the indices of elements in the window.
        Loop through the input list of numbers arr with an index i.
        In each iteration, pop elements from the deque q until the deque is empty or the value of the last element in the deque is less than or equal to the current element arr[i].
        Append the index i to the deque q.
        If the first element in the deque q is equal to i - k, then pop it from the deque, since it is outside the current window.
        If i is greater than or equal to k - 1, append the value arr[q[0]] to the result list, which represents the maximum value in the current window.
        Return the result list after the loop.
        """
        result = []
        q = deque()
        
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            
            if q[0] == i - k:
                q.popleft()
            
            if i >= k - 1:
                result.append(nums[q[0]])
        return result