class Solution:
    '''
    Traverse secret and guess to find the "bulls". Also, store the number of occurrences of every digit (0~9) in secret and guess in two arrays d1 and d2. 
    The # of 0 in guess that are in secret = min(d1[0], d2[0]); the # of 1 in guess that are in secret = min(d1[1], d2[1]); ... So, the # of digits in guess that are in secret = min(d1[0], d2[0]) + min(d1[1], d2[1]) + ... + min(d1[9], d2[9]). 
    The # of "cows" = the # of digits in guess that are in secret - the # of digits in guess that are in secret and are located in the correct position = the # of digits in guess that are in secret - the # of "bulls". 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def getHint(self, secret: str, guess: str) -> str:
        numBulls = 0
        d1, d2 = [0] * 10, [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                numBulls += 1
            d1[int(secret[i])] += 1
            d2[int(guess[i])] += 1
        
        numCows = 0
        for digit in range(10):
            numCows += min(d1[digit], d2[digit])
        numCows -= numBulls
        
        return str(numBulls) + 'A' + str(numCows) + 'B'