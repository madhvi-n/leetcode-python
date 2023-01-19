class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if a%3 ==0 and a%5==0 else "Fizz" if a%3 == 0 else "Buzz" if a%5==0 else str(a) for a in range(1, n + 1)]