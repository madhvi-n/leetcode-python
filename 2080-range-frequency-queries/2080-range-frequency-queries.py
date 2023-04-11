class RangeFreqQuery:
    
    def __init__(self, arr):
        self.map = defaultdict(list)
        for i, a in enumerate(arr):
            self.map[a].append(i)

    def query(self, left, right, a):
        i = bisect.bisect(self.map[a], left - 1)
        j = bisect.bisect(self.map[a], right)
        return j - i


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)