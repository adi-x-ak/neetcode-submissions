class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashSet<Character> seen = new HashSet<>();
       //left pointer 
        int l=0;
        //to store result 
        int result=0;
        //loop through r pointer 
        for(int r=0; r<s.length();r++){
           // if at the particular index already seen remove it from the set and move left pointer 
            while(seen.contains(s.charAt(r))){
                seen.remove(s.charAt(l));
                l++;
            }
            //ifnot add the character to set 
            seen.add(s.charAt(r));
            //calculate the length of window ayt the particular point and return the max length
            result= Math.max(result, r-l+1);

        }
        return result;
        
    }
}
