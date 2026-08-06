class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dix = set()

        for i in nums:
            if i in dix:
                return True
            else:
                dix.add(i)
        
        return False