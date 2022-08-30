class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startIndex = 0
        current = 0

        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        for i in range(n):
            current += gas[i] - cost[i]
            if current < 0:
                startIndex = i + 1
                current = 0
        return startIndex