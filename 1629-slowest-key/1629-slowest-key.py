class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
#         hashmap = dict()
#         hashmap[keysPressed[0]] = releaseTimes[0]
        
#         for i in range(1, len(releaseTimes)):
#             current_duration = releaseTimes[i] - releaseTimes[i-1]
#             current_key = keysPressed[i]
#             hashmap[current_key] = max(current_duration, hashmap.get(current_key, 0))
        
#         slowest_key = ''
#         longest_duration = 0
        
#         for key, duration in hashmap.items():
#             if duration > longest_duration:
#                 slowest_key, longest_duration = key, duration
#             elif duration == longest_duration and key > slowest_key:
#                 slowest_key = key
#         return slowest_key
    
        ansKey = keysPressed[0]
        ansDuration = releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            duration = releaseTimes[i] - releaseTimes[i-1]
            if duration > ansDuration or duration == ansDuration and key > ansKey:
                ansKey = key
                ansDuration = duration
        return ansKey