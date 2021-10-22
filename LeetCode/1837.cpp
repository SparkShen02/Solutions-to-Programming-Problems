class Solution {
public:
    /*
    Steps for converting an integer num from base 10 to another base k:
        1. Get the remainder num % k. This remainder is the first (i.e., least siginicant) digit of the new number in the other base; 
        2. num = num // k
        3. Repeat the process until num == 0
    */
    int sumBase(int num, int k) {
        int ans = 0;
        while (num > 0) {
            ans += num % k; 
            num /= k; 
        }
        return ans; 
    }
};