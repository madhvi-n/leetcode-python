class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        
        for a, b in trust:
            indegree[a] -= 1
            indegree[b] += 1

        for i in range(1, n + 1):
            if indegree[i] == n - 1:
                return i
        return -1