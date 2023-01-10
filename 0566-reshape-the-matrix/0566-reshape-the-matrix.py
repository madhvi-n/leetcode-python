class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        elements = []
        matrix = []

        for rows in mat:
            elements.extend(rows)
        
        if len(elements) != r * c:
            return mat
        
        for i in range(0, len(elements), c):
            matrix.append(elements[i:i+c])
        return matrix
        
        