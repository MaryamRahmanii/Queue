import heapq


class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None


    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)


class Priority_queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item,priority):
        heapq.heappush(self.elements,(priority,item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.elements)[1]
        else:
            return None

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

class Circular_queue:
        def __init__(self,max_size):
            self.maxsize:max_size
            self.queue= [None] * max_size
            self.front=0
            self.rear=0
            self.size=0

        def enqueue(self, item):
            self.queue[self.rear]=item
            self.rear=(self.rear+1)%self.maxsize
            self.size+=1

        def dequeue(self):
            if not self.is_empty():
                item=self.queue[self.front]
                self.queue[self.front]=None
                self.front=(self.front+1)%self.maxsize
                self.size-=1
                return item
            else:
                return None

        def is_empty(self):
            return self.size == 0

        def Size(self):
            return self.size







