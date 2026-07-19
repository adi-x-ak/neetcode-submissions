class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ''' we need to create an adacency list to store courses and their follwing pre requsites'''
        ''' we create a visit set keep track of current nodes in dfs tarck
            if we something agagin in the stack it means we have seen cycle
            for evevry course we persom dfs to check if it can be compelted or not 
            during dfs 
            base case 1 if its already in the visited we return false 
            if its course preq list is empty we can rteurn true 

            if both of them doesnt satisfy 
            add the current course to visit list 
            recursively check the pre req
            if any othe pre req returns false immediately return false 
            or else remove from the course
            emppty the courses pre req list and return true 

            now the main part is loop through courses in hasmap
            cann dfs  function if not dfs return false else true '''

        preMap={i:[] for i in range(numCourses)}
        for crc,pre in prerequisites:
            preMap[crc].append(pre)
        visiting= set()
        def dfs(crc):
            if crc in visiting:
                return False 
            if preMap[crc] ==[]:
                return True 
            
            visiting.add(crc)
            for pre in preMap[crc]:
                if not dfs(pre):
                    return False
            visiting.remove(crc)
            preMap[crc]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True