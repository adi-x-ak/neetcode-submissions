from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)>len(s):
            return ""

        countT = defaultdict(int)
        window = defaultdict(int)

        for ch in t:
            countT[ch] +=1

        need = len(countT)
        have = 0

        res = ""
        resLen = float("inf")

        l = 0

        for r in range(len(s)):

            ch = s[r]

            window[ch] +=1

            if ch in countT and window[ch] == countT[ch]:
                have +=1

            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                leftChar = s[l]
                window[leftChar] -=1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -=1

                l+=1

        return res

    





                    
                    

                




        