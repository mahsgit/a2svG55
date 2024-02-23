class MyStack:

    def __init__(self):
        self.que1=deque()

        

    def push(self, x: int) -> None:
        self.que1.append(x)

    def pop(self) -> int:
         val=self.que1.pop()
         return val
        
        

    def top(self) -> int:
         val=self.que1[-1]
         return val
        

    def empty(self) -> bool:
        if not self.que1:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()