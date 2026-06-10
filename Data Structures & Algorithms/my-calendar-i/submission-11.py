class CalendarNode:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.L = None
        self.R = None

class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
            if not self.root:
                self.root = CalendarNode(startTime, endTime)
                return True
            
            return self.bookHelper(self.root, startTime, endTime)

    def bookHelper(self, root, startTime, endTime):
        if not (endTime <= root.startTime or startTime >= root.endTime):
            return False
        
        if endTime <= root.startTime:
            if not root.L:
                root.L = CalendarNode(startTime, endTime)
                return True
            return self.bookHelper(root.L, startTime, endTime)
        
        if not root.R:
            root.R = CalendarNode(startTime, endTime)
            return True
        return self.bookHelper(root.R, startTime, endTime)




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)