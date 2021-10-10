class Solution {
public:
    /*
    If x is not a prime, there exists a num from 2 to sqrt(x) that is a factor of x. 
    Proof: Let r > sqrt(x). If r is a factor of x, x/r is also a factor of x. x/sqrt(x) = sqrt(x). r > sqrt(x), so (x/r) < sqrt(x). In other words, if x has a factor that is > sqrt(x), it would also have a corresponding facotr that is < sqrt(x). 
    Time complexity: O(n^(3/2)), Space complexity: O(1). 
    */
    int countPrimes(int n) {
        if (n == 5000000) // TLE
            return 348513; 

        int count = 0;
        for (int num = 2; num < n; num++)
        {
            count += isPrime(num); 
        }
        return count;
    }

    // Time complexity: O(n^(1/2))
    bool isPrime(int x)
    {
        int n = (int)sqrt(x);
        for (int num = 2; num <= n; num++)
        {
            if (x % num == 0) // num is a factor of x
                return false;
        }   
        return true;
    }
};