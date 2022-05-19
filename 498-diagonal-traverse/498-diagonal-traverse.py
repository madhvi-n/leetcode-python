class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
       (r, c) [r+c]
       (0, 0) [0] => 1
       (0, 1) [1] => 2
       (1, 0) [1] => 4
       
       (2, 0) [2] => 7
       (1, 1) [2] => 5
       (0, 2) [2] => 3
       
       (1, 2) [3] => 6
       (2, 1) [3] => 8
       (2, 2) [4] => 9
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        hashmap = collections.defaultdict(list)
        
        if not matrix: 
            return result
        
        for row in range(rows):
            for col in range(cols):
                hashmap[row+col].append(matrix[row][col])
        
        for key, values in hashmap.items():
            # if key is even, reverse the values
            if values:
                if key % 2 == 0:
                    result.extend(values[::-1])
                else:
                    result.extend(values)
        return result