class Solution:
    def trap(self, height: List[int]) -> int:
        '''algorithm the idea is two have two pointers left at the beginning and right at the ending
        since we know the limiting factor is lowest of maximun of both sides we try to get only leftmax or right max 
        '''
        l=0
        r=len(height)-1
        leftmax=height[l]
        rightmax=height[r]
        result=0

        #two pointers until eithe rof them cross paths 
        while l<r:
            if leftmax<=rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                result+=leftmax-height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                result+=rightmax-height[r]
        return result

        