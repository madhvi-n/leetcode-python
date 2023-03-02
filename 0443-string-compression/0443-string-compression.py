class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        
        while i < len(chars):
            groupLen = 1
            
            while i + groupLen < len(chars) and chars[i + groupLen] == chars[i]:
                groupLen += 1
            chars[res] = chars[i]
            res += 1
            if groupLen > 1:
                str_repr = str(groupLen)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += groupLen
        
        return res
        
        