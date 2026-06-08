class CalendarNode:
    def __init__(self, st, et):
        self.startTime = st
        self.endTime = et
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
        if not(startTime >= root.endTime or endTime <= root.startTime):
            return False

        if endTime <= root.startTime:
            if root.L is None:
                root.L = CalendarNode(startTime, endTime)
                return True
            return self.bookHelper(root.L, startTime, endTime)
        else:
            if root.R is None:
                root.R = CalendarNode(startTime, endTime)
                return True
            return self.bookHelper(root.R, startTime, endTime)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)