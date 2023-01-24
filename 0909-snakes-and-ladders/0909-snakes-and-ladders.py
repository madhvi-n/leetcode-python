class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited = set([1])
        N = len(board)
        up = N ** 2
        queue = [(1,0)]
        hashmap = dict()
        initial = 1
        flip = False
        for i in range(N):
            if not flip:
                for j in range(N):
                    hashmap[initial] = (N-1-i, j)
                    initial += 1
            else:
                for j in range(N):
                    hashmap[initial] = (N-1-i, N-1-j)
                    initial += 1
            flip = not flip
        
        while queue:
            nums, distance = queue.pop(0)
            if nums == up:
                return distance
            
            for cell in range(nums + 1, min(nums+6, up)+1):
                if cell not in visited:
                    visited.add(cell)
                    r, c = hashmap[cell]
                    
                    if board[r][c] == -1:
                        queue.append((cell,distance + 1))
                    else:
                        queue.append((board[r][c], distance + 1))
        return -1