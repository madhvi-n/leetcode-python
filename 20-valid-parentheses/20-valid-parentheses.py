class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        config = {"(": ")", "[": "]", "{": "}"}
        
        for i, v in enumerate(s):
            if v in config.keys():
                stack.append(v)
            else:
                if stack:
                    paren = stack[-1]
                    stack.pop()
                    if config.get(paren) != v:
                        return False

                else:
                    return False

        return True if not stack else False