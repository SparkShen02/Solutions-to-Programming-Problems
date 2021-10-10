class Solution:
    '''
    Sort times by arrival times. 
    Use a min heap (unoccupiedChairs) to store unoccupied chairs and a min heap (occupiedChairs) to store occupied chairs & their return times. 
    When a friend arrives, release from occupiedChairs the chairs that are no longer occupied and add them to unoccupiedChairs. Then, allocate the unoccupied chair with the smallest number to the friend. 
    Time complexity: O(nlog(n)), Space complexity: O(n). 
    '''
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        times.sort()
        unoccupiedChairs = [i for i in range(len(times))]
        heapq.heapify(unoccupiedChairs)
        occupiedChairs = []

        for i in range(len(times)):            
            while len(occupiedChairs) != 0 and occupiedChairs[0][0] <= times[i][0]:
                _, chair = heapq.heappop(occupiedChairs)
                heapq.heappush(unoccupiedChairs, chair)
            
            curChair = heapq.heappop(unoccupiedChairs)
            if times[i] == target:
                return curChair
            heapq.heappush(occupiedChairs, (times[i][1], curChair))