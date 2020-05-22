class Stack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        return self.data[-1]

    def pop(self):
        return self.data.pop()

    def peek(self):
        l = len(self.data)
        return self.data[l-1]

    def __str__(self):
        return self.data.__str__()


