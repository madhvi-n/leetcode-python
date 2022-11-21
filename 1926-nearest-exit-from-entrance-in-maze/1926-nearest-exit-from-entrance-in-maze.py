class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(*entrance, 0)]) #row, col, distance
        visited = set([tuple(entrance)])
        
        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            
            if curr_distance != 0 and any([curr_row == 0, curr_col == 0, curr_row == rows - 1, curr_col == cols - 1]):
                return curr_distance
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_row, next_col = curr_row + dx, curr_col + dy
                
                if not 0 <= next_row < rows or not 0 <= next_col < cols:
                    continue
                
                if maze[next_row][next_col] == "." and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, curr_distance + 1))
        return -1
                    
        