class MinStack:
    # solution is O(1) for each operation for time
    # space: O(N) for input
    def __init__(self):
        # create empty stack
        self.stack = []
        # create empty minStack
        self.minStack = []

    def push(self, val: int) -> None:
        # push to the stack
        self.stack.append(val)
        # check minStack is empty
        if len(self.minStack) < 1:
            # true -> push to minStack
            self.minStack.append(val)
        else:
            # else -> check if val is less than or equal to  top of minStack -> if true -> push val
            if val <= self.minStack[-1]:
                self.minStack.append(val)
            else:
                #   -> if val is less than top of minStack -> push top value of minStack to minStack
                self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        #pop the top value of stak
        self.stack.pop()
        # pop the top value of minStack
        self.minStack.pop()

    def top(self) -> int:
        # return the top value of stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # return the top value of minStack        
        return self.minStack[-1]        
