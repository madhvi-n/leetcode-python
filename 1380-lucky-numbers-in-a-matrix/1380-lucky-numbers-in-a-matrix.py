class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # create sets of row min and col max
        row_min = set()
        col_max = set()
        
        # get min in each rows
        for row in matrix:
            row_min.add(min(row))
        
        # zip(*matrix) returns cols of matrix, get max in each cols
        for col in zip(*matrix):
            col_max.add(max(col))
        
        # return intersection of two sets
        return list(row_min & col_max)
            