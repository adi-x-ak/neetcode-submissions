class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''algorithm
        1)lopp through the strings seperately 
        2) add in hash map 
        3)compare two hashmaps 
        4)if same return true else false '''
        map1 = {} # this how we define hashmap in python
        map2 = {}
        
        for i in range(len(s)):
            element = s[i]
            if element in map1:
                map1[element]+=1
            else:
                map1[element] =1
        for j in range(len(t)):
            element = t[j]
            if element in map2:
                map2[element]+=1
            else:
                map2[element] =1
        if map1==map2:
            return True
        else:
            return False
        

        
             
                
            
    
    
        

         
        