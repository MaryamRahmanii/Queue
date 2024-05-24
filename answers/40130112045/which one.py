class whichone:
    def __init__(self,input):
        self.queue={}
        for chr in input:
            self.queue[chr]=ord(chr)

    def enqueue(self,item):
        self.queue[item]=ord(item)

    def dequeue(self):
        if not self.is_empty():
            max_item=max(self.queue,key=self.queue.get)
            del self.queue[max_item]
            return max_item
        else:
            return None

    def print(self):
        for item in sorted(self.queue,key=self.queue.get,reverse=True):
            print(item,end=" ")

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)


input_string='ARYAN'

priorityqueue=whichone(input_string)

priorityqueue.print()
