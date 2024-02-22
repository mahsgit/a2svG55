class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        print(path)
        ans=[]
        for i in path:
            if i=='..':
                if ans:
                    ans.pop()
                    ans.pop()

            elif i=='.' or i=="":
                continue
            else :
                ans.append('/')
                ans.append(i)
            print(ans)
        if not ans :
            return"/"
        else:
          return "".join(ans)
      
        
            
        