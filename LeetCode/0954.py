class Solution:
    '''
    The problem actually asks whether it's possible to group the array into len(arr)/2 pairs, such that in each pair, one integer = 2 * the other integer. 
    Algorithm: 
        Traverse arr, and use a dictionary to store the number of occurrences of each integer in arr. 
        Sort arr. 
        Traverse arr, and try to group each integer num with its larger counterpart (i.e., num / 2 if num < 0 and num * 2 if num >= 0). 
    This algorithm works because:
        The smallest integer must be grouped with its larger counterpart (because its smaller counterpart doesn't exist in arr); then, discarding the first group that has been formed, the next smallest integer must be grouped with its larger counterpart (because its smaller counterpart doesn't exist in arr); ...
    Time complexity: O(nlogn), Space complexity: O(n). 
    '''
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        # arr.sort()
        # for num in arr: 
        #     if freq[num] == 0:
        #         continue
        #     # Try to group num with its larger counterpart
        #     counterpart = num / 2 if num < 0 else num * 2
        #     if counterpart not in freq or freq[counterpart] == 0:
        #         return False
        #     freq[num] -= 1
        #     freq[counterpart] -= 1

        for num in sorted(list(freq.keys())):
            if freq[num] == 0:
                continue
            counterpart = num / 2 if num < 0 else num * 2
            if counterpart not in freq or freq[counterpart] < freq[num]:
                return False
            freq[counterpart] -= freq[num]
        return True