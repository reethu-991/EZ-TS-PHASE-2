import queue
a=queue.Queue()
b=queue.Queue()
for x in range(5):
    b.put(x)
print(a.empty())
print(b.empty())
import queue
l=queue.Queue(maxsize=5)
l.put(10)
l.put(20)
print(type(l))
