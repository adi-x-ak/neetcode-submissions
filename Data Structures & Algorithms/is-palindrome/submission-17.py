class Solution:
    def isPalindrome(self, s: str) -> bool:
        #intilaize l,r
        l,r=0,len(s)-1
        while l<r:
            #lets write two while conditions for the letter to be a valid one 
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            #comapre two chararcters 
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

        