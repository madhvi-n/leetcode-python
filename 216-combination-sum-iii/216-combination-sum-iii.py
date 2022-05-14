class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, cap)
                    for comb in helper(k-1, n-last, last)]
        return helper(k, n, 10)