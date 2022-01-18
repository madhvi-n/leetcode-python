class Solution:
    def reachNumber(self, target: int) -> int:
        move, steps = 1, 1
        
        target = abs(target)

        while target > steps:
            move += 1
            steps += move

        if target%2 == steps%2:
            return move
        return move + move%2 + 1