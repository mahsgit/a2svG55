class Solution:
    def balancedString(self, s: str) -> int:
        value=Counter(s)
        check=Counter()
        v=len(s)//4
        ans=float('inf')
        l=0
        for key in value:
            if value[key]>v:
                check[key]+=value[key]-v
        if not check :
            return 0
        else:
            for r in range(len(s)):
                if s[r] in check:
                    check[s[r]]-=1
                    while max(check.values())<=0:
                        ans=min(ans,r-l+1)
                        if s[l] in check:
                            check[s[l]]+=1
                        l+=1
            return ans

