class KStacks:
  def __init__(self, k, size) -> None:
    self.k = k
    self.size = size
    self.arr = [0] * size
    self.top = [-1] * k
    self.next = [i + 1 for i in range(size)] # -1 means: this is the last element
    self.next[size-1] = -1
    self.free = 0

  def __str__(self):
    items = ['{!r}'.format(item) for item in self.arr]
    return '[' + ', '.join(items) + ']'

  def isEmpty(self, stackNumber):
    return self.top[stackNumber] == -1

  def isFull(self):
    return self.free == -1

  def push(self, item, stackNumber):
    if self.isFull():
      return False
    
    insertAt = self.free
    self.arr[insertAt] =  item
    self.free = self.next[insertAt]

    self.next[insertAt] = self.top[stackNumber] 
    self.top[stackNumber] = insertAt
    
    return True

  def pop(self, stackNumber):
    if self.isEmpty(stackNumber):
      return -1
    
    topOfStack = self.top[stackNumber]
    self.top[stackNumber] = self.next[topOfStack]
    self.next[topOfStack] = self.free
    self.free = topOfStack

    return self.arr[topOfStack]
  

  def printstack(self, sn):
    top_index = self.top[sn]
    while (top_index != -1):
        print(self.arr[top_index])
        top_index = self.next[top_index]


if __name__ == "__main__":
     
    # Create 3 stacks using an 
    # array of size 10.
    kstacks = KStacks(3, 10)
    print(kstacks, kstacks.next)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    print(kstacks, kstacks.next)
    kstacks.push(45, 2)
    print(kstacks, kstacks.next)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)
    print(kstacks, kstacks.next)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    kstacks.push(55, 2)
    print(kstacks, kstacks.next)

 
    print("Popped element from stack 2 is " +
                         str(kstacks.pop(2)))
    print("Popped element from stack 1 is " +
                         str(kstacks.pop(1)))
    print("Popped element from stack 0 is " +
                         str(kstacks.pop(0)))
 
    print(kstacks)
