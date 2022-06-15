class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        indegree = dict()
        topological_order = []

        for dest, src in prerequisites:
            adjacency_list[src].append(dest)
            indegree[dest] = 1 + indegree.get(dest, 0)

        queue = deque([k for k in range(num_courses) if k not in indegree])

        while queue:
            vertex = queue.popleft()
            topological_order.append(vertex)

            if vertex in adjacency_list:
                for node in adjacency_list[vertex]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        queue.append(node)
        return topological_order if len(topological_order) == num_courses else []