class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        i=1
        while i<len(arr) and arr[i]>arr[i-1]:
            i+=1
        if i==1 or i==len(arr):
            return False
        while i<len(arr ) and arr[i]<arr[i-1]:
            i+=1
        if i==len(arr):
            return True
        else:
            return False
        # return i==len(arr)
      


  

        

       

          
        