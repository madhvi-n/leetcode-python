class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashmap = defaultdict(set)
        
        for user, time in logs:
            hashmap[user].add(time)
        
        res = [0] * k
        
        for values in hashmap.values():
            if len(values) <= k:
                res[len(values) - 1] += 1
        return res