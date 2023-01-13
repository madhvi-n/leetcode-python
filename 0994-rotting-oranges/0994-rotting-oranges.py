class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        
        # count fresh and mark rotten cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    rotten.add((r, c))
        
        levels = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while rotten:
            levels += 1
            temp = set()
            
            for x, y in rotten:
                for dx, dy in directions:
                    row, col = x + dx, y + dy
                    
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        temp.add((row, col))
            rotten = temp
        
        return max(levels - 1, 0) if fresh == 0 else -1
            