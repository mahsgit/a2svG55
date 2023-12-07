class Solution:
    def largestGoodInteger(self, num: str) -> str:
        out = ""
        i = 0
        while i < len(num) - 2:
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                out = max(out, num[i:i+3])
                i += 3
            else:
                i += 1
        return out

        