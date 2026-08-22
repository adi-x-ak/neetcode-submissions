class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the intervas by the first
        intervals.sort(key=lambda i:i[0])
        result=0

        prevsend=intervals[0][1]

        for i in range(1, len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]

            if start<prevsend:
                result+=1
                prevsend=min(prevsend,end)
            else:
                prevsend=end
        return result

            