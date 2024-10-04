
import threading

class RingBuffer:
  def __init__(self, capacity=10) -> None:
    self.buffer = [None] * capacity
    self.capacity = capacity
    self.tail = 0
    self.head = 0
    self.count = 0
    #self.lock = threading.Lock()

  def __str__(self):
    items = ['{!r}'.format(item) for item in self.buffer]
    return '[' + ', '.join(items) + ']'

  def enqueue(self, item):
    print(f'{threading.current_thread().name}: enqueue {item}')
    if self.isFull():
      return
    #self.lock.acquire()
    self.buffer[self.tail] = item
    self.tail = (self.tail + 1) % self.capacity
    #self.lock.release()
    self.count += 1
    return True

  def dequeue(self):

    if self.isEmpty():
      return
    
    item = self.buffer[self.head]
    #self.lock.acquire()
    self.buffer[self.head] = None
    self.head = (self.head + 1) % self.capacity
    #self.lock.release()
    self.count -= 1
    print(f'{threading.current_thread().name}: dequeue: {item}')

    return item

  def isEmpty(self):
    return self.tail == self.head
  
  def isFull(self):
    return self.count == self.capacity

rb = RingBuffer(3)
rb.enqueue(1)
print('dequeue ', rb.dequeue())

rb.enqueue(2)
rb.enqueue(3)
rb.enqueue(4)
print(rb)