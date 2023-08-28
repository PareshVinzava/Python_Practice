class StackTOPn:
    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join([str(i) for i in self.items])

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def Display_all_items(self):
        return (self.items)

s = StackTOPn()

print(s.isEmpty())

s.push('first')
s.push('second')
s.push('third')

print(s)

print(s.peek())

print(s.Display_all_items())



