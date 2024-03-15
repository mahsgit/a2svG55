class Solution:
    def arrangeWords(self, text: str) -> str:
        words=text[0].lower() + text[1:]
        ans=list(map(str,words.split()))

       
        return " ".join(sorted(ans,key=len)).capitalize()
    
        