class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary2 = salary[1:-1]
        add=sum(salary2)
        return add/len(salary2)