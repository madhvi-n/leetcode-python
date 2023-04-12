class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        left_sorted = sorted(enumerate(intervals), key=lambda v: (v[1][0], v[0]))  # v = index, (start, end)
        ans = [-1] * len(intervals)
        heap = []
        
        for idx, (start, end) in left_sorted:
            heapq.heappush(heap, (end, idx))
            while heap and heap[0][0] <= start:  # heap[0][0] = right bound of smallest value on the heap
                _, left_idx = heapq.heappop(heap)
                ans[left_idx] = idx
        return ans