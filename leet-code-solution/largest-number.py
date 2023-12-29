class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools 
        nums=list(map(str,nums))

        def compare(one,two):
            if one+two>two+one:
                return 1
            elif one+two<two+one:
                return -1
            else:
                return 0
        

        numss=sorted(nums,key=functools.cmp_to_key(compare), reverse=True)
        a="".join(numss)
        a=int(a)
        return str(a)