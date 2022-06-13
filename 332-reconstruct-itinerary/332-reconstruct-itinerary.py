class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        route = []

        for x, y in tickets:
            graph[x].append(y)

        for key in graph:
            graph[key] = sorted(graph[key], reverse=True)

        def dfs(src):
            while graph[src]:
                candidate = graph[src].pop()
                dfs(candidate)
            route.append(src)

        dfs("JFK")
        return route[::-1]