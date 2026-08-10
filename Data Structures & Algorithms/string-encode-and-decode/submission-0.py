class Solution:

    def encode(self, strs: List[str]) -> str:
        encoderx= ""
        for word in strs:
            encoderx += str(len(word)) + "#" + word

        return (encoderx)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])

            result.append(s[j+1:j+1+ length])

            i = j+1+length
        return result


