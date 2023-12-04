class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out=""
        i=j=0
        len_1=len(word1)
        len_2=len(word2)
        while i< len_1 and j<len_2:
            out+=word1[i]
            out+=word2[j]
            i+=1
            j+=1
        while i<len_1:
            out+=word1[i]
            i+=1
        while j<len_2:
            out+=word2[j]
            j+=1
        return out


    