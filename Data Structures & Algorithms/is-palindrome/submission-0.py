class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowr = s.lower()
        takespaces = lowr.split(" ")

        print(takespaces)
        return takespaces == takespaces.reverse()