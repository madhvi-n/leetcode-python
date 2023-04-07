class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
         we can use a hashmap to count the number of rabbits that gave the same answer. 
         Then, we can iterate over the hashmap and for each count, we can calculate the number of 
         groups of rabbits with the same color that could have given that count. 
         Finally, we can add up all the groups to get the total number of rabbits.
        """
        count = dict()
        for a in answers:
            if a not in count:
                count[a] = 1
            else:
                count[a] += 1
        min_rabbits = 0
        for a, c in count.items():
            min_rabbits += math.ceil(c / (a + 1)) * (a + 1)
        return min_rabbits