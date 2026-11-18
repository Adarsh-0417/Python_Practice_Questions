class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for ch in s:
            if ch.isalnum():
                word += ch.lower()
        reverse = word[::-1]
        if word == reverse:
            return True
        else:
            return False
