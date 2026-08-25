class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dicx = {}

        for string in strs:
            key = "".join(sorted(string))

            if key in dicx:
                dicx[key].append(string)
            else:
                dicx[key] = [string]
        
        return list(dicx.values())
