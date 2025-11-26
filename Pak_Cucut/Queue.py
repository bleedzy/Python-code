class LinearQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print("Queue penuh, tidak bisa enqueue!")
        else:
            self.queue.append(item)
            print(f"{item} dimasukkan ke queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong, tidak bisa dequeue!")
            return None
        else:
            item = self.queue.pop(0)
            print(f"{item} dikeluarkan dari queue")
            return item

    def display(self):
        print("Isi Queue:", self.queue)

class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Circular Queue penuh!")
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        print(f"{item} dimasukkan ke circular queue")

    def dequeue(self):
        if self.is_empty():
            print("Circular Queue kosong!")
            return None

        item = self.queue[self.front]

        if self.front == self.rear:
            # Hanya ada satu elemen
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size

        print(f"{item} dikeluarkan dari circular queue")
        return item

    def display(self):
        if self.is_empty():
            print("Circular Queue kosong!")
            return

        print("Isi Circular Queue:", end=" ")

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.max_size
        print()


Q = LinearQueue(5)
Q.enqueue('A')
Q.enqueue('B')
Q.enqueue('C')
Q.display()
Q.dequeue()
Q.display()

CQ = CircularQueue(5)
CQ.enqueue(10)
CQ.enqueue(20)
CQ.enqueue(30)
CQ.display()
CQ.dequeue()
CQ.display()
