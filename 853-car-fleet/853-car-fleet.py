class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in reversed(sorted(zip(position, speed))):
            dist = target - pos
            if not stack:
                stack.append(dist / vel)
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)