class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Create the Frequency Map from Array:
        frequency_map = dict()
        for num in arr:
            frequency_map[num] = 1 + frequency_map.get(num, 0)

        heap = []
        for value in frequency_map.values():
            heapq.heappush(heap, -value)

        # Here, Start popping num out of the heap till we reach at least half the length of the array, then return the count.
        count = 0  # <= The least number of elements we need to remove
        total = 0  # <= The frequency count of elements we are removing
        half_size = len(arr) // 2
        while total < half_size:
            count += 1
            real_value = -heapq.heappop(heap)
            freq = real_value
            total += real_value
        return count
        
        