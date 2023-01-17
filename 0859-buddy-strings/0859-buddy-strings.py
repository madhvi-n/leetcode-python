class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        m, n = len(s), len(goal)
        if m != n:
            return False
        
        # case 1: eg: ("aa", "aa") -> check if any char occurs twice
        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False
        
        # case 2: check if there are exactly 1 pair of differing indices
        diffs = []
        cnt = 0
        for i in range(m):
            x, y = s[i], goal[i]
            
            if x != y:
                diffs.append((i, x, y))
                cnt += 1
        
        if cnt != 2:
            return False
        
        _, x1, y1 = diffs[0]
        _, x2, y2 = diffs[1]
        return x1 == y2 and x2 == y1
        
        