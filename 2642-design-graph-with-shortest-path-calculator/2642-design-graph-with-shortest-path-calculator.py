class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)

        for src, dest, cost in edges:
            self.graph[src].append((dest, cost))
        

    def addEdge(self, edge: List[int]) -> None:
        src, *rest = edge 
        self.graph[src].append(rest)

    def shortestPath(self, node1: int, node2: int) -> int:
        seen = set()
        heap = [(0, node1)]
        while heap:
            cost, node = heappop(heap)
            if node == node2:
                return cost
            
            if node not in seen and node in self.graph:
                seen.add(node)
                for child, cost1 in self.graph[node]:
                    heappush(heap, (cost + cost1, child))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)