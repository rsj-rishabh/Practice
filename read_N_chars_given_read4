# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
from collections import deque

class Solution:
    def __init__(self):
        self.bufQueue = deque()
        
    def read(self, buf: List[str], n: int) -> int:
        buf4 = ['']*4
        
        # if buffer queue already has n elements
        if n <= len(self.bufQueue):
            print('buffer queue already has n elements')
            print(self.bufQueue)
            i = 0
            while i < n:
                buf[i] = self.bufQueue.popleft()
                i += 1
        else:
            # fill the buffer queue
            print('buffer queue does not have n elements')
            while len(self.bufQueue) < n:
                print(self.bufQueue)
                t = read4(buf4)
                if t == 0:
                    # reached EOF
                    print('reached EOF')
                    i = 0
                    # fill buffer and return
                    print(len(self.bufQueue))
                    bq = len(self.bufQueue)
                    while i < bq:
                        buf[i] = self.bufQueue.popleft()
                        i += 1
                    print(i)
                    return bq
                else:
                    # fill buffer queue
                    for i in range(t):
                        self.bufQueue.append(buf4[i])
            print(self.bufQueue)
            # fill buffer
            i = 0
            while i<n:
                buf[i] = self.bufQueue.popleft()
                i += 1
                
        return n
