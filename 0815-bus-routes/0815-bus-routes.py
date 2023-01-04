class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        route_graph = defaultdict(list)

        for bus, route in enumerate(routes):
            for dest in route:
                route_graph[dest].append(bus)
        
        queue = [(source, 0)]
        seen = set([source])
        for stop, bus in queue:
            if stop == target: 
                return bus
            
            for i in route_graph[stop]:
                for j in routes[i]:
                    if j not in seen:
                        queue.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  # seen route
        return -1
        