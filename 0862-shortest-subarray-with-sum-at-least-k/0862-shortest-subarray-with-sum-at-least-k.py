class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix = [0]
        
        for x in nums:
            prefix.append(prefix[-1] + x)

        ans = N + 1 # N+1 is impossible
        queue = collections.deque() #opt(y) candidates, represented as indices of P
        for y, num in enumerate(prefix):
            #Want opt(y) = largest x with Px <= Py - K
            while queue and num <= prefix[queue[-1]]:
                queue.pop()

            while queue and num - prefix[queue[0]] >= k:
                ans = min(ans, y - queue.popleft())

            queue.append(y)

        return ans if ans < N+1 else -1