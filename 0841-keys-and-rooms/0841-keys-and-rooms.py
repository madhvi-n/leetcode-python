class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for index, room in enumerate(rooms):
            graph[index].extend(room)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    dfs(child)

        dfs(0)
        return len(visited) == len(rooms)