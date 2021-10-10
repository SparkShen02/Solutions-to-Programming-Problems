class Solution {
public:
    /*
    Recursion. All possible strings of S can be obtained by appending its first character (both lowercase and uppercase if it's a letter) to the front of all possible strings of S.substr(1). 
    Time complexity: O(2^n * n), Space complexity: O(2^n * n). Explanation: there are 2^n resulting strings. Each string has a length of n (i.e. it's constructed in n steps). 
    */
    vector<string> letterCasePermutation(string S) {
        vector<string> ans;

        if (S.size() == 0)
        {
            ans.push_back("");
            return ans; 
        }

        char ch = S.at(0);
        ans = letterCasePermutation(S.substr(1)); 
        int size = ans.size(); 
        for (int i = 0; i < size; i++)
        {
            if (isalpha(ch)) // ch is a letter
            {
                char chLow = tolower(ch);
                ans.push_back(chLow + ans[i]);
                char chUp = toupper(ch);
                ans[i] = chUp + ans[i]; 
            }
            else 
            {
                ans[i] = ch + ans[i]; 
            }
        }
        return ans; 
    }
};