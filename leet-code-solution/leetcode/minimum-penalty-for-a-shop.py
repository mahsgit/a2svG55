class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers=list(customers)
        customers.append('l')
        count=Counter(customers)
        left=0
        var=0
        inde=0
        mini=float('inf')
        for i,val in enumerate(customers):

            if val=='Y':
                var+=count['Y']
                count['Y']-=1
                var+=left

            elif val=='N':
                var+=left
                left+=1
                var+=count['Y']
                


            elif val=='l':
                var+=left

            if var<mini:
                mini=min(mini,var)
                inde=i
            var=0


        

        
        return inde