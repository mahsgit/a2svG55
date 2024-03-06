class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

            val=bisect_left(letters,target)
            if val==len(letters) or letters[-1]==target:
                return letters[0]
            else:
                while letters[val]==target:
                    val+=1

                return letters[val]
            # return "c"


        