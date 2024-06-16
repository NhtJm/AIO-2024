class MyQueue:
    def __init__(self, capacity):
        self.queue1 = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue1) == 0

    def is_full(self):
        return len(self.queue1) == self.capacity

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue1.pop(0)

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return None
        self.queue1.append(item)

    def front(self):
        if self.is_empty():
            return None
        return self.queue1[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
# >> False
print(queue1.front())
# >> 1
print(queue1.dequeue())
# >> 1
print(queue1.front())
# >> 2
print(queue1.dequeue())
# >> 2
print(queue1.is_empty())
# >> True
