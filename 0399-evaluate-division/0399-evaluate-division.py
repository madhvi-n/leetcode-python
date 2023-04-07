class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         graph = defaultdict(tuple)
        
#         def add_edge(f, t, value):
#             if f in graph:
#                 graph[f].append((t, value))
            
#         for vertices, value in zip(equations, values):
#             f, t = vertices
#             add_edge(f, t, value)
#             add_edge(t, f, 1/value)
        
#         def find_path(query):
#             b, e = query
            
#             if b not in graph or e not in graph:
#                 return -1.0
                
#             queue = collections.deque([(b, 1.0)])
#             visited = set()
            
#             while queue:
#                 front, cur_product = queue.popleft()
#                 if front == e:
#                     return cur_product
#                 visited.add(front)
#                 for neighbor, value in graph[front]:
#                     if neighbor not in visited:
#                         queue.append((neighbor, cur_product * value))
            
#             return -1.0
        
#         build_graph(equations, values)
#         return [find_path(q) for q in queries]

        # Step 1: precompute values and store in hashmap
        graph = defaultdict(dict)
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        # Step 2: evaluate queries using hashmap
        results = []
        for numerator, denominator in queries:
            if numerator not in graph or denominator not in graph:
                results.append(-1.0)
            elif numerator == denominator:
                results.append(1.0)
            else:
                visited = set()
                stack = [(numerator, 1.0)]
                found = False
                while stack and not found:
                    node, curr_value = stack.pop()
                    visited.add(node)
                    for neighbor, edge_value in graph[node].items():
                        if neighbor == denominator:
                            results.append(curr_value * edge_value)
                            found = True
                            break
                        elif neighbor not in visited:
                            stack.append((neighbor, curr_value * edge_value))
                if not found:
                    results.append(-1.0)

        return results