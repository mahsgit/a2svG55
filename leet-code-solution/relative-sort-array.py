class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        # answer=[]
        # for i in arr2:
        #     while i in arr1:
        #         answer.append(i)
        #         arr1.remove(i)
        # return (answer+sorted(arr1))

        arrmap = {}
        for i, value in enumerate(arr2):
            arrmap[value] = i

        arr1.sort(key=lambda x: (arrmap[x] if x in arrmap else len(arr2), x))
        return arr1
        