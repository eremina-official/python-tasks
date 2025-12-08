class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def peek(self):
        '''
        Retrun the last item without removing it
        '''
        return self.data[-1]

