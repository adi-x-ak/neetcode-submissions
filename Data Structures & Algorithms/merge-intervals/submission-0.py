class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #we need to first sort the list based on first insex 

        intervals.sort(key=lambda i:i[0])
        #lets create an output array and add the first element 
        output = [intervals[0]]

        #lets loop through the remaning array sincle the firste lement is already there we start from the second

        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            #now extract the last end of the laste element in the output array

            lastend = output[-1][1]

            #now the main logic if is start is small than lastend we merge the intervals (always rember take max while merging )
            if start<=lastend:
                output[-1][1] = max(lastend,end)
            else:
                output.append([start , end])
        return output