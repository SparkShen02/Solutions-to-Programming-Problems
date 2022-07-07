class Solution:
    '''
    Count the total number of satisfied customers if the technique is not used. 
    Then, use a sliding window to count: for each minute, the number of unsatisfied customers who will turn satisfied if the technique is used at that minute.
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        def isGrumpy(i):
            return grumpy[i] == 1

        # Count the total number of satisfied customers if the technique is not used
        n = len(customers)
        numSatisfied = 0
        for i in range(n):
            if not isGrumpy(i):
                numSatisfied += customers[i]
        
        # Count the number of unsatisfied customers who will turn satisfied if the technique is used at the first minute
        numUnsatisfied = 0
        for i in range(minutes):
            if isGrumpy(i):
                numUnsatisfied += customers[i]

        # Count the same for every minute and record the maximum
        maxUnsatisfied = numUnsatisfied
        for startMin in range(1, n-minutes+1):
            prevMin, endMin = startMin-1, startMin+minutes-1
            if isGrumpy(prevMin):
                numUnsatisfied -= customers[prevMin]
            if isGrumpy(endMin):
                numUnsatisfied += customers[endMin]
            maxUnsatisfied = max(maxUnsatisfied, numUnsatisfied)
        
        return numSatisfied + maxUnsatisfied