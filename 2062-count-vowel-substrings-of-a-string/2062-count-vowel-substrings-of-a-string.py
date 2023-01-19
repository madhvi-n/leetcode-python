class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        maps = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        # k and i are two pointers in typical same direction sliding window problem, j is used to mark start point
        j, k, vowel, res = 0, 0, 0, 0
        
        for i in range(len(word)):
            if word[i] in maps:
                maps[word[i]] += 1
                
                if maps[word[i]] == 1:
                    vowel += 1
                
                while vowel == 5:
                    maps[word[k]] -= 1
                    if maps[word[k]] == 0:
                        vowel -= 1
                    k += 1
                res += k - j
            else:
                # reset pointers and maps
                maps = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
                vowel = 0
                j, k = i+1, i+1
        return res