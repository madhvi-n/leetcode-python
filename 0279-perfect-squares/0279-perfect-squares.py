class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque()
        visited = set()
        queue.append((0, 0))
        
        while queue:
            s, count= queue.popleft()
            count += 1
            
            for i in range(1, n+1):
                temp = s + i * i
                if temp > n:
                    break
                if temp == n:
                    return count
                
                if temp not in visited:
                    visited.add(temp)
                    queue.append((temp,count))