from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashMap, res, pStart, sStart = defaultdict(int), [], len(p), len(s)
        if pStart > sStart : return []

        # build hashmap for pattern
        for character in p:
            hashMap[character] += 1

        # initial full pass over the window
        for i in range(pStart - 1):
            if s[i] in hashMap:
                hashMap[s[i]] -= 1

        # slide the window with stride 1
        for i in range(-1, sStart - pStart + 1):
            if i > -1 and s[i] in hashMap:
                hashMap[s[i]] += 1

            if i + pStart < sStart and s[i + pStart] in hashMap:
                hashMap[s[i + pStart]] -= 1

            # check whether we encountered an anagram
            if all(v == 0 for v in hashMap.values()):
                res.append(i + 1)

        return res