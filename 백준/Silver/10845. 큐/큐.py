class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.is_empty():
            return -1
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if self.is_empty():
            return -1
        return self.queue[0]

    def back(self):
        if self.is_empty():
            return -1
        return self.queue[-1]

N = int(input())
commands = []
for _ in range(N):
    commands.append(input())
queue = Queue()
for command in commands:
    c = command.split()
    if c[0] == 'push':
        queue.enqueue(int(c[1]))
    elif c[0] == 'pop':
        print(queue.dequeue())
    elif c[0] == 'size':
        print(queue.size())
    elif c[0] == 'empty':
        print(int(queue.is_empty()))
    elif c[0] == 'front':
        print(queue.front())
    elif c[0] == 'back':
        print(queue.back())