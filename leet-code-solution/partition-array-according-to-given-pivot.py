class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        more=[]
        equal=[]
        for i in nums:
            if i>pivot:
                more.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                less.append(i)
        less.extend(equal)
        less.extend(more)
        return less


        