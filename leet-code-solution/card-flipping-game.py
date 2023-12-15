class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int: 

        forbidden=set()
        both_list= set(fronts + backs)
        current_min=float('inf')
        for back ,front in zip(fronts,backs):
            if back == front:
                forbidden.add(back)

        for i in both_list:
            if i not in forbidden:
                current_min=min(i,current_min)
        if current_min==float('inf'):
            return 0
        else:
            return current_min
    

        

               
        


        