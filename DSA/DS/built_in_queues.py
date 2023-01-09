# using collections module
from collections import deque

collections_queue = deque(maxlen=3)
collections_queue.append(1)
collections_queue.append(2)
collections_queue.append(3)
collections_queue.popleft()
print(collections_queue)