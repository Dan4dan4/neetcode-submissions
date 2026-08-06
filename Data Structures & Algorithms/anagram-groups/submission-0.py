class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dix= {}

        for string in strs:
            key = "".join(sorted(string))
            if key in dix:
                dix[key].append(string)
            else:
                dix[key] = [string]
        
        return list(dix.values())
