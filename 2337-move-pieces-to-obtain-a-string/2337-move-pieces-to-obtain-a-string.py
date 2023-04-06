class Solution:
    def canChange(self, start: str, target: str) -> bool:
        lcnt, rcnt = 0, 0
        for c1, c2 in zip(start, target):
            if c1 == 'L': lcnt += 1
            if c2 == 'L': lcnt -= 1
            if c1 == 'R': rcnt += 1
            if c2 == 'R': rcnt -= 1
        if lcnt or rcnt: 
            return False
        
        s_ptr = 0
        for t_ptr in range(len(target)):
            if target[t_ptr] == '_':
                continue
            else:
                while s_ptr < len(start) and start[s_ptr] == '_':
                    s_ptr += 1
                if (target[t_ptr] != start[s_ptr] or
                    target[t_ptr] == 'L' and s_ptr < t_ptr or
                    target[t_ptr] == 'R' and s_ptr > t_ptr):
                    return False
                s_ptr += 1
        return True