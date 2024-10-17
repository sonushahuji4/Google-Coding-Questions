# https://leetcode.com/problems/minimum-time-difference/description/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def getTimeToMinutes(time):
            hours, minutes = map(int,time.split(":"))
            return hours*60 + minutes
        
        minutesList = [getTimeToMinutes(time) for time in timePoints]
        minutesList.sort()

        minDiff = float('inf')

        for i in range(1, len(minutesList)):
            diff = minutesList[i] - minutesList[i - 1]
            minDiff = min(minDiff, diff)
        
        circularDiff = (minutesList[0] + 1440) - minutesList[-1]
        minDiff = min(minDiff, circularDiff)

        return minDiff

        
