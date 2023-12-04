class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = ''
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i+2])
                out += chr( num + ord('a')-1  )
                i += 3
            else:
                num = int(s[i])
                out += chr(num + ord('a') - 1)
                i += 1
        return out

        