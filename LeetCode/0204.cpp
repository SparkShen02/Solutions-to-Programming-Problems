class Solution {
public:
    /*
    If x is a prime, then 2x, 3x, 4x, ... are not prime. 
    If y is not a prime, then there exists x < y such that x is prime and y is a multiple of x (proof can be found online). 
    Use an array isPrime of length n to record whether a number is prime or not. Iterate num from 2 to n-1, isPrime[num] would indicate whether num is prime or not. If num is prime, then record in isPrime that 2*num, 3*num, ... are not prime. 
    Time complexity: O(nlog(log(n))) (proof can be found online), Space complexity: O(n). 
    */
    int countPrimes(int n) {
        vector<bool> isPrime(n, true); // initialize a vector of length n with true as the default values
        
        for (int num = 2; num < n; num++) {
            if (isPrime[num]) {
                for (int c = 2; c * num < n; c++)
                    isPrime[c*num] = false; 
            }
        }

        int ans = 0; 
        for (int i = 2; i < n; i++)
            ans += isPrime[i]; 
        return ans; 
    }

    /*
    Method 2: TLE

    // If x is not a prime, there exists a num from 2 to sqrt(x) that is a factor of x. 
    // Proof: Let r > sqrt(x). If r is a factor of x, x/r is also a factor of x. x/sqrt(x) = sqrt(x). r > sqrt(x), so (x/r) < sqrt(x). In other words, if x has a factor that is > sqrt(x), it would also have a corresponding facotr that is < sqrt(x). 
    // Time complexity: O(n^(3/2)), Space complexity: O(1). 
    int countPrimes(int n) {
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
    */
};
