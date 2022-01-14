import heapq

class Solution:
    '''
    Store all candidates for the next smallest pair in a priority queue (implemented using heap) named pq. Repeatedly (for k times), pop the next smallest pair (u, v) from pq, record it, and push (u+1, v), (u, v+1) to pq. To avoid duplicates in pq, Use a set to record all pairs that have been added to it. 
    Proof that all possible pairs are considered in this way: 
        Suppose (u, v) is an arbitrary pair. (u, v) is considered if (u-1, v) is considered, if (u-2, v) is considered, ..., if (0, v) is considered, if (0, v-1) if considered, ..., if (0, 0), which is the first pair, is considered. 
    Time complexity: O(klog(k)), Space complexity: O(k). 
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        heapq.heappush(pq, (0, 0, 0)) # a pair is represented by such a tuple: (sum, nums1 index, nums2 index)
        added = set()
        ans = []
        for _ in range(k):
            if len(pq) == 0:
                break
            _, u, v = heapq.heappop(pq)
            ans.append([nums1[u], nums2[v]])
            if u+1 < len(nums1) and (u+1, v) not in added:
                heapq.heappush(pq, (nums1[u+1]+nums2[v], u+1, v))
                added.add((u+1, v))
            if v+1 < len(nums2) and (u, v+1) not in added:
                heapq.heappush(pq, (nums1[u]+nums2[v+1], u, v+1))
                added.add((u, v+1))
        return ans