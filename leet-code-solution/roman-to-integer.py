class Solution:
    def romanToInt(self, s: str) -> int:
        num_map={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_num = 0
        num=""
        for i in s[::-1]:
            num=num_map[i]

            if num >=prev_num:
                result+=num
            else:
                result-=num
            prev_num=num
        return result



