class Solution:
    '''
    All possible lengths: k * shorter, (k-1) * shorter + longer, (k-2) * shorter + 2 * longer, ..., k * longer.
    Time complexity: O(n), Space complexity: O(n).
    '''
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]

        ans = []
        for i in range(k+1):
            ans.append((k-i) * shorter + i * longer)
        return ans