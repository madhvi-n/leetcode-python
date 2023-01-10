class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        hashmap = dict()

        def paths(i, j):
            if i >= row or j >= col or obstacleGrid[i][j] == 1:
                return 0
            
            if(i==row-1 and j==col-1):
                return 1

            if (i,j) in hashmap:
                return hashmap[(i,j)]

            c = 0

            c += paths(i,j + 1) + paths(i + 1,j)
            hashmap[(i,j)] = c
            return c

        res = paths(0, 0)
        return res