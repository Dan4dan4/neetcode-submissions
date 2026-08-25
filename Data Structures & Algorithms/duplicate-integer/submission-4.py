class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        lister = []

        for num in nums:
            if num in lister:
                return True
            else:
                lister.append(num)
        
        return False