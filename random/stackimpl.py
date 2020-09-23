

class stackimpl:
    def __init__(self):
        self.description = 'this is a stack implementation'
        self.items= []


    def pop(self):
        self.items.pop()


    def push(self,item):
        self.items.append(item)


    def peek(self):
        return self.items[len(self.items)-1]


    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()




