class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1

        while n > 0:
            remainder = n % 10
            product *= remainder
            total += remainder
            n //= 10

        return product - total