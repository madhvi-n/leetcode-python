class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [0] * numCourses

        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i, visited):
            # if ith node is marked as being visited, then a cycle is found
            if visited[i] == -1:
                return False

            # if it is done visted, then do not visit again
            if visited[i] == 1:
                return True

            # mark as being visited
            visited[i] = -1

            # visit all the neighbours
            for j in graph[i]:
                if not dfs(j, visited):
                    return False

            # after visit all the neighbours, mark it as done visited
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i, visited):
                return False
        return True