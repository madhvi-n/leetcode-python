class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Create dictionaries to store the rows and columns of each stone
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        
        for i, (x, y) in enumerate(stones):
            row_dict[x].append(i)
            col_dict[y].append(i)

        # Use DFS to find the groups of stones
        visited = set()
        groups = 0
        for i in range(len(stones)):
            if i not in visited:
                stack = [i]
                while stack:
                    j = stack.pop()
                    visited.add(j)
                    for k in row_dict[stones[j][0]] + col_dict[stones[j][1]]:
                        if k not in visited:
                            stack.append(k)
                groups += 1

        # The maximum number of stones that can be removed is the total number of stones minus the number of groups
        return len(stones) - groups
        
        