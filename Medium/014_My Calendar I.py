# https://leetcode.com/problems/my-calendar-i/description/

# Approach One
class MyCalendar:

    def __init__(self):
        self.calender = []
        

    def book(self, start: int, end: int) -> bool:
        if len(self.calender) == 0:
            self.calender.append([start, end])
            return True
        else:
            for event in self.calender:
                startEventDate, endEventDate = event
                if start < endEventDate and end > startEventDate: return False
            self.calender.append([start, end])
            return True


# Approach Two
class MyCalendar:
    def __init__(self):
        self.calender = []
    
    def binarySearch(self, start, end):
        low, high = 0, len(self.calender)
        while low < high:
            mid = low + (high - low) // 2
            startEvent, endEvent = self.calender[mid]
            # Compare with the start of the event at mid
            if startEvent < start:
                low = mid + 1
            else:
                high = mid
        return low
    
    def book(self, start: int, end: int) -> bool:
        position = self.binarySearch(start, end)
        
        # Check overlap with the previous event
        if position > 0:
            startEventPrev, endEventPrev = self.calender[position - 1]
            if start < endEventPrev:  # Overlap with the previous event
                return False
        
        # Check overlap with the next event
        if position < len(self.calender):
            startEventNext, endEventNext = self.calender[position]
            if end > startEventNext:  # Overlap with the next event
                return False
        
        # No overlap, insert the event
        self.calender.insert(position, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
