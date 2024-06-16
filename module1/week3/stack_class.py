class MyStack:
    def __init__(self, capacity):
        self.stack1 = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack1) == 0

    def is_full(self):
        return len(self.stack1) == self.capacity

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack1.pop()

    def push(self, item):
        if self.is_full():
            print("Stack is full")
            return False
        self.stack1.append(item)
        return True

    def top(self):
        if self.is_empty():
            return None
        return self.stack1[-1]


stack1 = MyStack(capacity=5)
stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)
stack1.push(5)
stack1.push(3)
stack1.push(4)
print(stack1.is_full())
# >> False

print(stack1.top())
# >>2

print(stack1.pop())
# >> 2
print(stack1.top())
# >> 1
print(stack1.pop())
# >> 1
print(stack1.is_empty())
# >> True
