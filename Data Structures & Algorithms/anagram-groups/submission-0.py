

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = []

        for i in range(len(strs)):
            tmp = {}
            for j in range(len(strs[i])):
                tmp[strs[i][j]] = 1 + tmp.get(strs[i][j],0)
            arr.append(tmp)

        for i in range(len(strs)):
            tmp = [strs[i]]

        ans = []

        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue
            
            tmp = [strs[i]]
            visited[i] = True

            for j in range(i+1,len(strs)):
                if arr[i]==arr[j]:
                    tmp.append(strs[j])
                    visited[j] = True

            ans.append(tmp)

        return ans







        