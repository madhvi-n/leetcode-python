class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = defaultdict(list)
#         visited = [0] * numCourses

#         for x, y in prerequisites:
#             graph[x].append(y)

#         def dfs(i, visited):
#             # if ith node is marked as being visited, then a cycle is found
#             if visited[i] == -1:
#                 return False

#             # if it is done visted, then do not visit again
#             if visited[i] == 1:
#                 return True

#             # mark as being visited
#             visited[i] = -1

#             # visit all the neighbours
#             for j in graph[i]:
#                 if not dfs(j, visited):
#                     return False

#             # after visit all the neighbours, mark it as done visited
#             visited[i] = 1
#             return True

#         for i in range(numCourses):
#             if not dfs(i, visited):
#                 return False
#         return True
            pre_map = {i: [] for i in range(numCourses)}

            for course, pre in prerequisites:
                pre_map[course].append(pre)

            visited = set()

            def dfs(course):
                if course in visited:
                    return False

                if not pre_map[course]:
                    return True

                visited.add(course)

                for pre in pre_map[course]:
                    if not dfs(pre):
                        return False
                visited.remove(course)
                pre_map[course] = []
                return True

            for course in range(numCourses):
                if not dfs(course):
                    return False
            return True
