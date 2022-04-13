class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst, i, j = list(s), 0, len(s) - 1
        while i < j:
            if not lst[i].isalpha():
                i += 1
            elif not lst[j].isalpha():
                j -= 1
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i, j = i + 1, j - 1
        return "".join(lst)