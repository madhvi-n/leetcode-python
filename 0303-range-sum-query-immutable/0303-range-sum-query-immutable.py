class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefixSum = [0] * (n+1)
        
        curr = 0
        for i in range(n):
            curr += nums[i]
            self.prefixSum[i+1] = curr

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + 1, right + 1
        return self.prefixSum[r] - self.prefixSum[l-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)