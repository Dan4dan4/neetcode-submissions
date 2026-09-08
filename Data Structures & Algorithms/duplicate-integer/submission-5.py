class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dicx = {}

        for num in nums:
            if num in dicx:
                return True
            else:
                dicx[num] =1
        
        return False