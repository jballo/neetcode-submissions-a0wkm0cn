class CalendarNode:
    def __init__(self, startTime, endTime):
        self.st = startTime
        self.et = endTime
        self.l = None
        self.r = None

def is_overlapping(s1, e1, s2, e2):
    return s1 < e2 and s2 < e1

class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root == None:
            self.root = CalendarNode(startTime, endTime)
            return True

        return self.book_helper(self.root, startTime, endTime)

    
    
    def book_helper(self, root, startTime, endTime):
        if is_overlapping(startTime, endTime, root.st, root.et):
            return False
        
        if endTime <= root.st:
            if not root.l:
                root.l = CalendarNode(startTime, endTime)
                return True
            return self.book_helper(root.l, startTime, endTime)
        elif startTime >= root.et:
            if not root.r:
                root.r = CalendarNode(startTime, endTime)
                return True
            return self.book_helper(root.r, startTime, endTime)

        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)