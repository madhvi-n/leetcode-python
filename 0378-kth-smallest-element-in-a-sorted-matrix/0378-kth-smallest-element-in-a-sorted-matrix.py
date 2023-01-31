class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return None
        
        n = len(matrix)
        
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        
        heapq.heapify(heap)
        
        for _ in range(k - 1):
            val, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return heap[0][0]