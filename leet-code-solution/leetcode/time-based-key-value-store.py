class TimeMap:

    def __init__(self):
        self.new=defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
       
        self.new[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
       
            ans=self.new[key]
            res=''
            l=0
            r=len(ans)-1
            while l<=r:
                mid=(l+r)//2
                if timestamp>=ans[mid][1]:
                    l=mid+1
                    res=ans[mid][0]

                else:
                    r=mid-1

            return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)