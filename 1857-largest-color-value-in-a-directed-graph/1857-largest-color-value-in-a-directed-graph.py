class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        # Build the graph and calculate the indegree of each node.
        graph = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            graph[v].append(u)
            indegree[u] += 1

        # Initialize the count dictionary for each node and the queue with nodes
        # that have zero indegree.
        count = [defaultdict(int) for _ in range(n)]
        queue = deque(filter(lambda i: not indegree[i], range(n)))

        # Traverse the graph using the queue.
        seen = 0
        ans = 0
        while queue:
            curr = queue.popleft()
            count[curr][colors[curr]] += 1
            ans = max(ans, count[curr][colors[curr]])
            seen += 1

            # Update the count dictionary for each neighbor of the current node.
            for v in graph[curr]:
                for c in count[curr]:
                    count[v][c] = max(count[v][c], count[curr][c])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        # If we have not seen all nodes, there is a cycle in the graph.
        if seen < n:
            return -1
        return ans