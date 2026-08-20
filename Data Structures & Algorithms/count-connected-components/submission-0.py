class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we need to build  an adjacency list first 
        graph=[[] for _ in range(n)]

        #build the grraph
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        #we need a set to keep trak of visited nodes 
        visited=set()
        #to keep track of number of components 
        components=0
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)







        #i need loop through each and every node if its not in visted we 
        #incerement the component and do a dfs call
        #dfs call recursively visitets all the componets that are connected 
        for nodes in range(n):
            if nodes not in visited:
                components+=1
                dfs(nodes)
        return components 
        