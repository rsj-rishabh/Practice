class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        if len(self.arr)>1:
            i = len(self.arr)-1
            while self.arr[i]<self.arr[i-1] and i>0:
                self.arr[i], self.arr[i-1] = self.arr[i-1], self.arr[i]
                i -= 1
        print(self.arr)
        
        return None
        

    def findMedian(self) -> float:
        n = len(self.arr)
        
        if n>1:
            if n % 2 == 0:
                return (self.arr[(n//2)]+self.arr[(n//2)-1])/2
            else:
                return self.arr[n//2]
        elif n == 1:
            return self.arr[0]
        else:
            return None


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
