class Solution:
    '''
    Use two pointers, one points to the start of current subarray, and the other points to the end of current subarray. 
    Use a set (hash table) to store the characters that are in the current subarray. Remove a character from the set when the "start" pointer moves forward, and add a character to the set when the "end" pointer moves forward. 
    Time complexity: O(n), Space complexity: O(n).
    '''
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxAns, curAns = nums[0], nums[0]
        start, end = 0, 0
        inSubarr = set()
        inSubarr.add(nums[0])
        while True:
            while end+1 < n and nums[end+1] not in inSubarr:
                end += 1
                curAns += nums[end]
                inSubarr.add(nums[end])

            maxAns = max(maxAns, curAns)
            if end+1 == n:
                return maxAns

            if start == end:
                start += 1
                end += 1
            else:
                curAns -= nums[start]
                inSubarr.remove(nums[start])
                start += 1