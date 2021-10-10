class Solution:
    '''
    Repeatedly compare the numbers in the two arrays and copy the smaller one to the merged array.
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []
        cur1, cur2 = 0, 0
        while cur1 < m and cur2 < n:
            if nums1[cur1] <= nums2[cur2]:
                merged.append(nums1[cur1])
                cur1 += 1
            elif nums1[cur1] > nums2[cur2]:
                merged.append(nums2[cur2])
                cur2 += 1

        if cur1 < m:
            merged += nums1[cur1:m]
        elif cur2 < n:
            merged += nums2[cur2:]
        
        nums1[:] = merged