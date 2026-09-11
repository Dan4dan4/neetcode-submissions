class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dicx= {}
        for n in nums:
            if n in dicx:
                return True
            else:
                dicx[n] = n
        
        return False