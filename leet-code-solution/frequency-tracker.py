class FrequencyTracker:

    def __init__(self):
           self.num_map = defaultdict(int)
           self.freq = defaultdict(int)
           self.max_frequency = 0
    def add(self, number: int) -> None:
        # self.num_map[number]= self.num_map.get(number,0)+1
        # self.num_map[number]+=1
        # self.freq[self.num_map[number]]+=1
        self.freq[self.num_map[number]] -= 1
        self.num_map[number] += 1
        self.freq[self.num_map[number]] += 1
        self.max_frequency = max(self.max_frequency, self.num_map[number])

    def deleteOne(self, number: int) -> None:
        # if self.num_map.get(number):
        #   self.num_map[number]-=1
          if self.num_map[number] > 0:
            self.freq[self.num_map[number]] -= 1
            self.num_map[number] -= 1
            self.freq[self.num_map[number]] += 1
            if self.freq[self.max_frequency] == 0:
                self.max_frequency -= 1



        

    def hasFrequency(self, frequency: int) -> bool:
        # if frequency  in self.num_map.values():
        #     return True
        # else:
        #     return False
         return frequency <= self.max_frequency and self.freq[frequency] > 0
    
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)