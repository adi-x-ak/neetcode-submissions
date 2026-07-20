class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        '''algorithm
        the idea is to store the preq along with their courses in hashmap

        loop through the pre reqsites and store each course with the respective pre req

        than create a visited set to keep track of dfs call stack 
        than lets write our dfs function 
        base cases are if we find anything during visted return false which means it has cycle 
        if the list is empty than we can say its true an ddoesnt have any pre req

        if not we add the course to set and call dfs function 
            if immediately any its returns false return false here also else 
            remove it from the set make the pre req empty 
            return tru 

        loop throuhh numcoueses if not dfs return false 
        return '''


        premap={i:[] for i in range(numCourses)}
        for crc,pre in prerequisites:
            premap[crc].append(pre)
        visting=set()

        def dfs(crc):
            if crc in visting:
                return False
            if premap[crc]==[]:
                return True
            visting.add(crc)
            for pre in premap[crc]:
                if not dfs(pre):
                    return False
            visting.remove(crc)
            premap[crc] =[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True