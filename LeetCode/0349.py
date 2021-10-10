class Solution:
    '''
    Traverse nums1 and record the numbers in a set. Then, traverse nums2, if reached a number that is in the set, add it to ans and remove it from the set.
    Time complexity: O(n), Space complexity: O(n).
    '''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numbers = set()
        ans = []
        for num in nums1:
            numbers.add(num)
        for num in nums2:
            if num in numbers:
                ans.append(num)
                numbers.remove(num)
        return ans