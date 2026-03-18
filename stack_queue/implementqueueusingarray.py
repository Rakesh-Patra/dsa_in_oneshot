class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item): # Renamed 'push' to 'enqueue' for clarity
        self.items.append(item)

    def dequeue(self): # Renamed 'pop' to 'dequeue'
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def size(self):
        return len(self.items)

# Testing the Queue
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.peek())  # Output: 10
print("Popped:", q.dequeue())      # Output: 10 (First in, first out)