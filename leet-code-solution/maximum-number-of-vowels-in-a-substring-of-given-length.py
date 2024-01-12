class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # v={'a','e','i','o','u'}
        v="aeiou"
        vowel=Counter(v)
        count=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        maxi=count
            
        for i in range(k,len(s)):
            if s[i] in vowel:
                count+=1
            if s[i-k]  in vowel:
                count-=1
            maxi=max(maxi,count)
        return maxi

       

           

        