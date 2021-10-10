public class Solution {
    /**
     * @param s: the given string
     * @return: whether this string is valid
     */
    public boolean checkValidString(String s) {
        int res=0;
        int count=0;
        if(s.substring(0,1).equals(")") || s.substring(s.length()-1,s.length()).equals("(")) return false;
        for(int i=0;i<s.length();i++){
            if(s.substring(i,i+1).equals("(")){res+=1;}
            else if(s.substring(i,i+1).equals("*")){count+=1;}
            else{
                res-=1;
            }
        }
        System.out.println(res);
        System.out.println(count);
        return res==0 || res<=count;
    }
}