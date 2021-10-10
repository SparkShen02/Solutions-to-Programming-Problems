class Solution {
public:
    /*
    Consider "ZY". Its corresponding column number = 25 (Y) * 26^0 + 26 (Z) * 26^1 = 701. 
    Time compelxity: O(1), Space complexity: O(1). 
    */
    int titleToNumber(string columnTitle) {
        int ans = 0; 
        long int k = 1; 
        for (int i = columnTitle.size() - 1; i > -1; i--) {
            ans += charToNumber(columnTitle[i]) * k; 
            k *= 26; 
        }
        return ans; 
    }

    int charToNumber(char ch) {
        return ch - 'A' + 1; 
    }
};