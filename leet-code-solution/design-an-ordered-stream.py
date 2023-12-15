class OrderedStream:

    def __init__(self, n: int):
      
        self.store = [None] * (n + 1) 
        self.pointer = 1
        
      
        

    def insert(self, idKey: int, value: str) -> List[str]:
  
        self.store[idKey] = value
        if idKey == self.pointer:
            while self.pointer < len(self.store) and self.store[self.pointer] is not None:
                self.pointer += 1
            return self.store[idKey:self.pointer]
        else:
            return []



        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
