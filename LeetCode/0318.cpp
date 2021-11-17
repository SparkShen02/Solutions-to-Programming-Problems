class Solution {
public:
    /*
    For each word, use each of the right-most 26 bits of a 32-bit variable to indicate whether it contains a certain letter. This makes checking whether two words share common letters a simple bitwise & operation. 
    Time complexity: O(n^2), Space complexity: O(n). 
    */
    int maxProduct(vector<string>& words) {
        int masks[words.size()]; 
        for (int i = 0; i < words.size(); i++) {
            masks[i] = 0; 
            string word = words[i]; 
            for (int j = 0; j < word.size(); j++) {
                masks[i] |= 1 << (word[j] - 'a');  
            }
        }

        int ans = 0; 
        for (int i = 0; i < words.size(); i++) {
            for (int j = i; j < words.size(); j++) {
                if ((masks[i] & masks[j]) == 0) { // they do not share common letters
                    int curAns = words[i].size() * words[j].size(); 
                    ans = curAns > ans ? curAns : ans; 
                }
            }
        }
        return ans; 
    }
};