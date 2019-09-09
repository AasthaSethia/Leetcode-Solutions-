class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x) == str(x)[::-1]
        return palindrome
