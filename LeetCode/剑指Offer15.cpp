class Solution {
public:
    /*
    Repeatedly compare (the bitwise & operation) n to 0...001, 0...010, 0...100 to see if a digit of n is 1. 
    Time complexity: O(1), Space complexity: O(1). 
    */
    int hammingWeight(uint32_t n) {
        int one = 1; // 0...001
        int ans = n & one;
        for (int i = 0; i < 31; i++) {
            one <<= 1; 
            if (n & one)
                ans += 1;
        }
        return ans; 
    }
};