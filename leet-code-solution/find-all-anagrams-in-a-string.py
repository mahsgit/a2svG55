class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=Counter(p)
        check=Counter(s[:len(p)])
        ans=[]
        count=0
        if check==target:
            ans.append(0)
        for i  in range(len(p),len(s)):
            check[s[i-len(p)]]-=1
            if check[s[i-len(p)]]==0:
                del check[s[i-len(p)]]
            check[s[i]]+=1
            if check==target:
                ans.append(i-len(p)+1)

        return ans






    

        