class RandomizedSet:

    def __init__(self):
        self.Map=set()
        

    def insert(self, val: int) -> bool:
        if val  not in self.Map:
            self.Map.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
           if val in self.Map:
                self.Map.remove(val)
                return True
           else:
                return False
        
        

    def getRandom(self) -> int:
        return random.choice(list(self.Map))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()