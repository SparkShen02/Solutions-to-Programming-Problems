class Solution {
public:
    /*
    An integer is a power of two if it's positive and the bits of its binary representation sum to 1. 
    Time complexity: O(1), Space complexity: O(1). 
    */
    bool isPowerOfTwo(int n) {
        if (n <= 0) {
            return false; 
        }
        int sum = 0; 
        for (int i = 0; i < 31; i++) {
            sum += n & 1;
            n >>= 1; 
        }
        return sum == 1; 
    }
};