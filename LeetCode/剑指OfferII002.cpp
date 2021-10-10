class Solution {
public:
    /*
    From right to left, add each two corresponding bits together. 
    Time complexity: O(n), Space complexity: O(n) (the resulting string).   
    */
    string addBinary(string a, string b) {
        int indA = a.size() - 1; int indB = b.size() - 1; 
        string ans = ""; 
        int addNext = 0; 
        while (indA >= 0 || indB >= 0) {
            int bitA = indA < 0 ? 0 : a[indA] - '0'; // if indA < 0, bitA = 0; else, bitA = a[indA] - '0'
            int bitB = indB < 0 ? 0 : b[indB] - '0'; 
            int addBit = bitA + bitB + addNext; 
            ans += '0' + addBit % 2; 
            addNext = addBit > 1 ? 1 : 0; 
            indA--; indB--; 
        }
        if (addNext == 1)
            ans += '1'; 
        reverse(ans.begin(), ans.end()); 
        return ans; 
    }
};