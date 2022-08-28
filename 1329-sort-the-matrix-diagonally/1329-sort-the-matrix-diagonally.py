class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        hashmap = defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                hashmap[i - j].append(mat[i][j])
        
        for k in hashmap:
            hashmap[k].sort(reverse=True)
        
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = hashmap[i - j].pop()
        return mat