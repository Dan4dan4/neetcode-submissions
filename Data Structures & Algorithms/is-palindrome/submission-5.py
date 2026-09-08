class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = s.lower()
        newstr = ""
        for char in cleaned:
            if char.isalnum():
                newstr += char

        return newstr == newstr[::-1]