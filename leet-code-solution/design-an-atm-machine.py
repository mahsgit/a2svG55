class ATM:

    def __init__(self):
        self.Map=[20,50,100,200,500]
        self.depositt=[0]*5

        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.depositt[i] += banknotesCount[i]

    

        

    def withdraw(self, amount: int) -> List[int]:
        result = [0] * 5
        for i in range(len(self.Map) - 1, -1, -1):
            used = min(amount // self.Map[i], self.depositt[i])
            result[i] = used
            amount -= used * self.Map[i]
        if amount != 0:
            return [-1]
        for i in range(len(self.Map)):
            self.depositt[i] -= result[i]
        return result
       
     
        
        
        



    

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
