class Solution {
public:
    /*
    Use two pointers, one points to the start of s and moves forward, while the other points to the end of s and moves backward. Repeatedly check if the two pointed chars are equal. 
    Time complexity: O(n), Space complexity: O(1).  
    */
    bool isPalindrome(string s) {
        int n = s.size(); 
        if (n == 0 or n == 1)
            return true; 

        int left = 0;
        int right = n - 1; 
        while (left < right) {
            // Skip useless chars
            while (left < right && !isalnum(s[left]))
                left += 1;
            while (left < right && !isalnum(s[right]))
                right -= 1;
            if (left >= right)
                break; 

            if (tolower(s[left]) != tolower(s[right]))
                return false; 
            left += 1;
            right -= 1;
        }
        return true; 
    }
};