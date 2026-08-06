class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ""

        for letter in s.lower():
            if letter.isalnum():
                clean += letter
        
        return clean == clean[::-1]