class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        lastsort=sorted(trips,key=lambda x: x[2])
        maxi=lastsort[-1][-1]
        new=[0]*(maxi+1)
        for i in range(len(trips)):
            val,l,r=trips[i]
            new[l]+=val
            new[r]-=val
        pref=[0]
        for i in range(len(new)):
            pref.append(pref[-1]+new[i])
        for i in range(len(pref)):
            if pref[i]>capacity:
                return False
        print(new)
        print(pref)


        return True

        




