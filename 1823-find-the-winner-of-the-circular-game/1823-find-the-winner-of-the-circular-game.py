class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = deque(range(1, n+1))
        
        while len(friends) > 1:
            for _ in range(k - 1):
                friends.append(friends.popleft())
            friends.popleft()
        return friends[0]
    
            