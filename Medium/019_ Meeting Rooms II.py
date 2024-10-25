# https://leetcode.com/problems/meeting-rooms-ii/description/

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervalsLength = len(intervals)
        if intervalsLength == 0: return 0
        intervals.sort(key=lambda x:x[0])

        minHeapFreeRooms = []
        heapq.heappush(minHeapFreeRooms,intervals[0][1])
        for (startTime, endTime) in intervals[1:]:
            if minHeapFreeRooms[0] <= startTime:
                heapq.heappop(minHeapFreeRooms)
            heapq.heappush(minHeapFreeRooms, endTime)
          
        return len(minHeapFreeRooms)
