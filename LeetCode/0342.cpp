class Solution {
public:
    /*
    An integer is a power of four if it's positive, the bits of its binary representation sum to 1, and the bit with the value 1 is an odd bit (the 1st bit, the 3rd bit, the 5th bit, ...). 
    Time complexity: O(1), Space complexity: O(1). 
    */
    bool isPowerOfFour(int n) {
        if (n <= 0) {
            return false; 
        }
        int sum = 0; 
        for (int i = 1; i < 32; i++) {
            if (n & 1) {
                if (i % 2 == 0)
                    return false; 
                sum += 1; 
            }
            n >>= 1; 
        }
        return sum == 1;
    }
};