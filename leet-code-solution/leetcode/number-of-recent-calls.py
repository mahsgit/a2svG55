class RecentCounter:

    def __init__(self):
        self.new=deque()        
    def ping(self, t: int) -> int:

        while self.new and self.new[0]<(t-3000) :
               self.new.popleft()
        self.new.append(t)

        return len(self.new)
       



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)