class MinStack:
    def __init__(self):
        self.st = []      # main stack
        self.min_st = []  # tracks minimums

    def push(self, val: int) -> None:
        self.st.append(val)

        # Push into min stack if it's a new minimum (or equal minimum).
        if not self.min_st or val <= self.min_st[-1]:
            self.min_st.append(val)

    def pop(self) -> None:
        # LeetCode guarantees valid operations, but this guard is harmless.
        if not self.st:
            return

        x = self.st.pop()
        if self.min_st and x == self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]