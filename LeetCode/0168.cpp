class Solution {
public:
    /*
    Sppose that column title = "@#&" and column number = ('&' - 'A' + 1) * 1 + ('#' - 'A' + 1) * 26 + ('@' - 'A' + 1) * 26^2. 
    Column number = ('&' - 'A') * 1 + ('#' - 'A') * 26 + ('@' - 'A') * 26^2 + 1 + 26 + 26^2. 
    Column number -= 1. 
    First, find '&', which = column number % 26 + 'A'. 
    Column number /= 26, which = ('#' - 'A') * 1 + ('@' - 'A') * 26 + 1 + 26. 
    Column number -= 1. 
    Second, find '#' ...
    Time complexity: O(log26(n)), Space complexity: O(log26(n)) (the resulting string). 
    */
    string convertToTitle(int columnNumber) {
        string ans = ""; 
        while (columnNumber > 0) {
            columnNumber--; 
            char cur = columnNumber % 26 + 'A';
            ans = cur + ans;  
            columnNumber /= 26; 
        }
        return ans; 
    }
};