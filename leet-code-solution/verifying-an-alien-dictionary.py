class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # prev=-1
        # for i in words:
        #     for j in range(len(i)):

        #        val= i[j] 
        #        current=order.find(val)
        #       if prev<current:

        #           words.sort(lambda i :i[0])
    

        newarr = sorted(words, key = lambda word: [order.index(word[i]) for i in range(len(word))])
     



        return newarr == words


        