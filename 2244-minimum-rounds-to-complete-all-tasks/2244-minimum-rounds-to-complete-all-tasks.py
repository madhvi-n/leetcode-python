class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hashmap = dict(Counter(tasks))
        
        if any(val == 1 for val in hashmap.values()):
            return -1

        rounds = 0
        arr = list(hashmap.values())

        while arr:
            curr = arr.pop()
            if curr > 3:
                arr.append(curr - 3)
            rounds += 1
        return rounds
