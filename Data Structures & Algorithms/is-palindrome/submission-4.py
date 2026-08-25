class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lower= s.lower()
        cleaned = ""

        for letter in lower:
            if  letter.isalnum():
                cleaned += letter
        
        return cleaned == cleaned[::-1]
