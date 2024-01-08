class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        n = len(s)
        i,j = 0,0
        letter = set()
        maxi = 0
        while(i<n):
            if s[i] not in letter:
                letter.add(s[i])
                i+=1
            else:
                letter.remove(s[j])
                j+=1
            if maxi < len(letter):
                maxi = len(letter)
        return maxi 
        