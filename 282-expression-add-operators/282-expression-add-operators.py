class Solution:
    def addOperators(self, expression: str, target: int) -> List[str]:
        def backtrack(i, path, diff, prev_num):
            if i == len(expression):
                if diff == target:
                    ans.append(path)
                return

            for j in range(i, len(expression)):
                if j > i and expression[i] == '0':
                    break  # Skip leading zero number

                num = int(expression[i:j + 1])
                if i == 0:
                    backtrack(j + 1, path + str(num), diff + num,
                              num)  # First num, pick it without adding any operator
                else:
                    backtrack(j + 1, path + "+" + str(num), diff + num, num)
                    backtrack(j + 1, path + "-" + str(num), diff - num, -num)
                    backtrack(j + 1, path + "*" + str(num), diff - prev_num + prev_num * num,
                              prev_num * num)  # Can imagine with example: 1+2*3*4

        ans = []
        backtrack(0, "", 0, 0)
        return ans