class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        
        queue = [(0, 0, k, 0)] #(row, col, k, steps)
        visited = set()
        
        while queue:
            x, y, k, steps = queue.pop(0)

            if x == rows-1 and y == cols-1: 
                return steps
            
            if (x, y, k) in visited: 
                continue
            
            visited.add((x, y, k))
            
            if grid[x][y]:
                if k >= 1: 
                    k -= 1
                else: continue

            for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                if 0 <= nx <= rows - 1 and 0 <= ny <= cols - 1:
                    queue.append((nx, ny, k, steps + 1))

        return -1      
        