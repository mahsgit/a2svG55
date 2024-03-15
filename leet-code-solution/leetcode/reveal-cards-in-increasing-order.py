class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        que=deque()
        que.append(deck[0])
        for val in deck[1:]:
            que.appendleft(que.pop())
            que.appendleft(val)
      

       
        return que

        