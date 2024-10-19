# https://leetcode.com/problems/rle-iterator/description/

# Approach One
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.index = 0
        self.encoded= self.getEncodedValuesList(encoding)
    
    def getEncodedValuesList(self,encoding):
        i = 0
        encodedValues = []
        while i < len(encoding)-1:
            steps = encoding[i]
            value = encoding[i+1]
            while steps != 0:
                encodedValues.append(value)
                steps -= 1
            i += 2
        return encodedValues


        

    def next(self, n: int) -> int:
        self.index += n
        if self.index >= len(self.encoded): return -1
        return self.encoded[self.index-1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

# Approach Two
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.index = 0
        self.encoding = encoding

    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            # Get the current count of repetitions for the value at self.index + 1
            count = self.encoding[self.index]
            if n > count:  # If we need to consume more than available in current batch
                # Reduce n by the number of available elements
                n -= count
                # Move to the next value
                self.index += 2
            else:
                # We can satisfy the request with the current value
                self.encoding[self.index] -= n
                return self.encoding[self.index + 1]
        
        # If we exit the loop, it means there are no more elements
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
