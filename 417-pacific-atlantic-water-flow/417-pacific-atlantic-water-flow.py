class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(row, col, visited, previous_height):
            if row < 0 or col < 0 or row == rows or col == cols or \
                    heights[row][col] < previous_height or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
        
        # water reaching the boundary cells of pacific and atlantic will reach the respective ocean
        # run dfs recursively on boundaries to find which cells allow the water to flow 
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])
        
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])
        
        # result = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) in pacific and (r, c) in atlantic:
        #             result.append([r, c])
        result = pacific.intersection(atlantic)
        return result