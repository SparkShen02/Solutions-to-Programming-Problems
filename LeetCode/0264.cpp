class Solution {
public:
    /*
    Each ugly number should be multiplied by 2, 3, and 5 to form a new ugly number. The key is to maintain the order of the numbers.
    Time complexity: O(n), Space complexity: O(1). 
    */
    long nthUglyNumber(long n) {
        long uglyNums[1690]; // n does not exceed 1690
        uglyNums[0] = 1;
        
        long* p2 = uglyNums; // track the number that is yet to be multiplied by 2
        long* p3 = uglyNums; // track the number that is yet to be multiplied by 3
        long* p5 = uglyNums; // track the number that is yet to be multiplied by 5
        for (int i = 1; i < n; i++)
        {
            long curUglyNum = min(min((*p2) * 2, (*p3) * 3), (*p5) * 5);
            uglyNums[i] = curUglyNum;
            
            if (curUglyNum == (*p2) * 2)
                p2++;
            if (curUglyNum == (*p3) * 3)
                p3++;
            if (curUglyNum == (*p5) * 5)
                p5++;
        }
        return uglyNums[n-1];
    }
};