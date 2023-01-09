class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def is_full(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
        else:
            self.list.append(value)
            return "Added"

    def pop(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = []

stack = Stack(3)
stack.push(12)
stack.push(14)
stack.push(55)
print(stack)