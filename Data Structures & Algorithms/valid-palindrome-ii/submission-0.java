class Solution {
    public boolean validPalindrome(String s) {
        //the idea is to do the regular palindrome 
        //the element that needs to be skipped is either from left or right 
        
        int i=0;
        int j = s.length()-1;
        while(i<j){
            if(s.charAt(i)!=s.charAt(j)){
                return isPalindrome(s , i+1 ,j) || isPalindrome(s,i,j-1);
            }
            i++;
            j--;
        }
        return true;

        
    }

    public boolean isPalindrome(String s , int i , int j){
        while(i<j){
            char ch1 = s.charAt(i);
            char ch2 = s.charAt(j);
            if(ch1!=ch2){
                return false;
            }
            else{
                i++;
                j--;
            }
        }

        return true;
    }
}