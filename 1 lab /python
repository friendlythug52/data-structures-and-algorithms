stack =
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)


#или 

class Stack:
  def __init__(self):
    self.top = None
    def push(self, data):
      new_node = Node(data)
      new_node.next = self.top
      self.top = new_node
    def pop(self):
      if not self.is_empty():
      popped = self.top
      self.top = self.top.next
      popped.next = None
