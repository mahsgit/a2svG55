class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        steps_list=[]
        for i in range(len(boxes)):
            s=0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    s+=abs(i-j)
            steps_list.append(s)
        return steps_list



        