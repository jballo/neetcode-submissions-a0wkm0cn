class MyStack:

    def __init__(self):
        # (exit) <- [...] <- (enter)
        self.first = [] # <- 2, 1 <-

    def push(self, x: int) -> None:
        self.first.append(x)

        for i in range(0, len(self.first) - 1):
            self.first.append(self.first.pop(0))

    def pop(self) -> int:
        return self.first.pop(0)

    def top(self) -> int:
        return self.first[0]

    def empty(self) -> bool:
        return len(self.first) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()