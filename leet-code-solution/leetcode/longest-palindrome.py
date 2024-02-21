class Solution:
    def longestPalindrome(self, s: str) -> int:
        new=Counter(s)
        total=0
        odd=0
        c=0
        print(new)
        for l,val in new.items():
            if val%2!=0:
                total+=val-1
                c=1
            else:
                total+=val

        return total+c
        