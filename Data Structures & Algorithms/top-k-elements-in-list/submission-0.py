class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dix = {}

        for num in nums:
            key= num
            if key in dix:
                dix[key] +=1
            else:
                dix[key] = 1
        
        sorteddix = sorted(dix, key=dix.get, reverse =True)

        return sorteddix[:k]
