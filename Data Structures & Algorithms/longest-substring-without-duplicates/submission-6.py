class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #start left pointer at zero index 
        left=0
        #i am using  a set datastructure to keep track of valid window
        window=set()
        #to keep track of longest length seen so far 
        length=0

        #loop through evevry alphabet in string 
        for right in range(len(s)):
             while s[right] in window:
                window.remove(s[left])
                left+=1
             window.add(s[right])
            #caluculate the length of cuurent window 
             windowsize=right-left+1
             length=max(length,windowsize)
        return length

        

        
        