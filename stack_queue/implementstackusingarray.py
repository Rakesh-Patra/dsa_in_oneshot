class stack:
    def __init__(self):
        self.items=[]
        

    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return "cannot pop in empty staack"
        else:
            return self.items.pop()
    def top(self):
        if len(self.items)==0:
            return "there is no top node in empty staack"
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
s = stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

print("Stack size:", s.size())     # 3
print("Top element:", s.top())     # 30

# Pop elements
print("Popped:", s.pop())          # 30
print("Popped:", s.pop())          # 20

print("Top now:", s.top())         # 10
print("Is empty?", s.is_empty())   # False

# Pop remaining
print("Popped:", s.pop())          # 10
print("Is empty?", s.is_empty())   # True

# Try popping empty stack
print("Popped:", s.pop())          # Error message
