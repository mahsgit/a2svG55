class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       num=int("".join(map(str, digits)))
       num=num+1
       final = [int(i) for  i in str(num)]
       return final
        