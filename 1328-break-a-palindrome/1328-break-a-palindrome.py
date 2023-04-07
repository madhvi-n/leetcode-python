class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        Start by iterating through the string from left to right until we find a non-'a' character. 
        We can then replace that character with 'a' and return the modified string.
        If we reach the end of the string without finding a non-'a' character, we can simply replace 
        the last character with 'b' to get the lexicographically smallest string that is not a palindrome.
        """
        n = len(palindrome)
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b' if n > 1 else ''