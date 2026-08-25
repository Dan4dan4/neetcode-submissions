class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dicx = {}

        for num in nums:
            if num in dicx:
                dicx[num] +=1
            else:
                dicx[num] =1
        
        return sorted(dicx,key=dicx.get, reverse= True)[:k]