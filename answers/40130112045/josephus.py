
class Cicular_queue:

    def __init__(self,max_size):
        self.maxsize: max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0


    def enqueue(self, item):
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % (self.max_size)
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            self.size -= 1
            return item
        else:
            return None

    def is_empty(self):
        return self.size == 0

    def Size(self):
        return self.size


def josephus(n,k):
    queue=Cicular_queue(max_size=n)

    for i in range(1,n+1):
        queue.enqueue(i)

    while queue.front != queue.rear:
        for _ in range(k-1):
            queue.enqueue(queue.dequeue())
            queue.dequeue()


    return queue.dequeue()




n=7
k=3

survivor=josephus(n,k)
print(survivor)