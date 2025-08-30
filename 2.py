class queue:
    def __init__(self,capacity):
        self.queue=[]
        self.capacity=capacity
    def enqueue(self,value):
        if len(self.queue)>=self.capacity:
            print("Queue overflow ! cannot enqueue", value)
        else:
            self.queue.append(value)
            print(value,"enqueued to queue.")
    def dequeue(self):
        if not self.queue:
            print("Queue underflow ! queue is empty.")
            return None
        else:
            return self.queue.pop(0)
    def front(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        else:
            return self.queue[0]
    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue elements:",self.queue)
q=queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:",q.dequeue())
q.display()
