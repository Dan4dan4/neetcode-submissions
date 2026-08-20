class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dix = {}
 

        for num in nums:
            if num in dix:
                dix[num] +=1
            else:
                dix[num] = 1
            
        return sorted(dix, key=dix.get, reverse=True)[:k]
        