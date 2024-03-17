class MyCircularQueue:

    def __init__(self, k: int):
        self.que=[]
        self.k=k
        

    def enQueue(self, value: int) -> bool:
        
         if not self.isFull():
             self.que.append(value)
             return True
        

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.que.pop(0)
            return True
        else:
            return False
        
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.que[0]
        

    def Rear(self) -> int:
         if self.isEmpty():
            return -1
         else:
            return self.que[-1]
        

    def isEmpty(self) -> bool:
        return len(self.que)==0
          
        

    def isFull(self) -> bool:
        return  len(self.que)==self.k
           
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()