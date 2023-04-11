class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Sort the people array in descending order of their heights.
        If two people have the same height, sort them in ascending order of their ki value.
        Iterate through the sorted people array, insert each person at the ki position in the result array.
        Return the result array.
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Initialize an empty list
        queue = []
       
        # Insert each person at the k-th position in the queue
        for p in people:
            queue.insert(p[1], p)
        return queue