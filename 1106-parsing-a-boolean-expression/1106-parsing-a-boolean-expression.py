class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        hashmap = {'&' : all, '|' : any, '!' : lambda x : not x[0]}
        
        stack = []
        for c in expression:
            if c in hashmap:
                stack.append(hashmap[c])
            elif c == '(':
                stack.append('(')
            elif c == 'f':
                stack.append(False)
            elif c == 't':
                stack.append(True)
                
            elif c == ')':
                ss = []
                while stack[-1] != '(':
                    ss.append(stack.pop())
                stack.pop()
                stack.append(stack.pop()(ss))
        return stack.pop()