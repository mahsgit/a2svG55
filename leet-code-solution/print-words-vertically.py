class Solution:
    def printVertically(self, s: str) -> List[str]:
        big = []
        maxi = 0
        inp = list(s.split(" "))
        for i in inp:
           maxi = max(len(i), maxi)

        for i in inp:
            maxi = max(len(i), maxi)

        for j in range(maxi):
            list1 = [i[j] if j < len(i) else ' ' for i in inp]
            big.append("".join(list1).rstrip())

        return big
