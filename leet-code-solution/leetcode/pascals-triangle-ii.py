class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
      if rowIndex==0:
          return [1]
      elif rowIndex==1:
          return [1,1]        

      array=self.getRow(rowIndex-1) 
      new=[1]   
      for i in range(1,len(array)):
          new.append(array[i]+array[i-1])
      new.append(1)
      return new





        

        