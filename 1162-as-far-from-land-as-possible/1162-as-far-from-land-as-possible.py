class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    queue.append((r, c))
        
        # no land or all land
        if not queue or rows * cols == len(queue):
            return -1
        
        visited = set()
        level = 0
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    
                    if 0 <= row < rows and 0 <= col < cols and not grid[row][col] and (row, col) not in visited:
                        visited.add((row, col))
                        queue.append((row, col))
            level += 1
        return level - 1