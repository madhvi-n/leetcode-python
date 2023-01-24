class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = 0
        n = len(ratings)
        
        front = [1] * n
        back = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                front[i] = front[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                back[i] = back[i + 1] + 1
        
        
        for i in range(n):
            total += max(front[i], back[i])
        
        return total
            