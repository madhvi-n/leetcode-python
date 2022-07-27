class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        
        # keep a track of rotten oranges and fresh oranges
        # why keep a track of fresh oranges? 
        # in case there are oranges which cannot be rottened by other oranges
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        levels = 0
        
        # for each rotten orange in queue
        # we explore in 4 directions
        #if explored cell is in bounds and has a fresh orange - change it to rotten,
        # reduce count of fresh and append the new rotten coordinates to queue
        # at the end, return levels - 1 if there are no fresh oranges left else -1
        
        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    r, c = x + dx, y + dy
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        queue.append((r, c))
        return -1 if fresh != 0 else max(levels - 1, 0)