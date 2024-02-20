class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*(n+1)
        for val in bookings:
            l,r,seat=val
            ans[l-1]+=seat
            ans[r]-=seat
        
        pref=[ans[0]]
        for i in ans[1:]:
            pref.append(pref[-1]+i)
        pref.pop()
        return pref