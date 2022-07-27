class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            curr = list(str(i))
            curr_sum = sum(int(i) for i in curr)
            if curr_sum % 2 == 0:
                count += 1
        return count