class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank or not end or not start or not bank:
            return -1
        
        if end in bank and len(bank) == 1:
            return 1
        
        length = len(start)
        
        genes = defaultdict(list)
        for gene in bank:
            for i in range(length):
                genes[gene[:i] + '*' + gene[i+1:]].append(gene)

        queue = deque([(start, 0)])
        seen = set(start)
        
        while queue:
            current, count = queue.popleft()
            if current == end:
                return count
            
            for i in range(length):
                possible_mutation = current[:i] + '*' + current[i+1:]
                
                for mutation in genes[possible_mutation]:
                    if mutation not in seen:
                        seen.add(mutation)
                        queue.append((mutation, count + 1)) 
        return -1