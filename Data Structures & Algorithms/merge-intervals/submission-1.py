class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #idea is to sort the given list based on the first index 
        intervals.sort(key= lambda i :i[0])

        #i will start by appending the first pair into the output 
        output=[intervals[0]]

        #now lets start loopinf from the second element 
        for i in range(1,len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]

            #above we have extracted start ans end lwts do the output 
            lastend=output[-1][1]
            #here we checking if start of current elemnt is less than the last one 
            if start<=lastend:
                output[-1][1]=max(lastend,end)
            else:
                output.append(intervals[i])
        return output



        