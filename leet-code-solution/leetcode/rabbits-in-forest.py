class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        check=Counter(answers)
        ans=0
        print(check)
        for val,c in check.items():
            if val>c:
                ans+=val+1
            else:
                
                ans+=ceil(c/(val+1))*(val+1)
               
        return ans
        