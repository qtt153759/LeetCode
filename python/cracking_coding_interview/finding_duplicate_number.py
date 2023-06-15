# Python3 program to print all Duplicates in array
 
# A class to represent array of bits using
# array of integers
class BitArray:
 
    # Constructor
    def __init__(self, n):
 
        # Divide by 32. To store n bits, we need
        # n/32 + 1 integers (Assuming int is stored
        # using 32 bits)
        self.arr = [0] * ((n >> 5) + 1)
 
    # Get value of a bit at given position
    def get(self, pos):
 
        # Divide by 32 to find position of
        # integer.
        self.index = pos >> 5
        # Now find bit number in arr[index]
        self.bitNo = pos & 0x1F
        print("check",pos,self.index, self.bitNo)
 
        # Find value of given bit number in
        # arr[index]
        return (self.arr[self.index] &
                   (1 << self.bitNo)) != 0
 
    # Sets a bit at given position
    def set(self, pos):
 
        # Find index of bit position
        self.index = pos >> 5
      
 
        # Set bit number in arr[index]
        self.bitNo = pos & 0x1F
        self.arr[self.index] |= (1 << self.bitNo)
 
# Main function to print all Duplicates
def checkDuplicates(arr):
 
    # create a bit with 32000 bits
    ba = BitArray(320000)
 
    # Traverse array elements
    for i in range(len(arr)):
 
        # Index in bit array
        num = arr[i]
 
        # If num is already present in bit array
        if ba.get(num):
            print(num, end = " ")
 
        # Else insert num
        else:
            ba.set(num)
 
# Driver Code
if __name__ == "__main__":
    arr = [1, 5, 1, 10, 12, 10]
    checkDuplicates(arr)
 
# This code is contributed by
# sanjeev2552