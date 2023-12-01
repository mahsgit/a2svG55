class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        out=""
        i=0
        while i<len(command):
            if command[i]=='G':
                out+=command[i]
            elif command[i]=='(':
                i+=1
                if command[i]==')':
                    out+='o'
                else:
                    out+="al"
            i+=1
        return out



        