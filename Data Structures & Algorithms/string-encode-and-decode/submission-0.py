class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        left = 0             #left pointer at index 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])   #it will get the number before the hash which is the length
            left = right + 1    #after the hash
            right = left + length   #complete the word
            res.append(s[left:right])
            left = right     #put left and right pointer after the word
        return res

