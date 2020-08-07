#Binary Reversal
#Have the function BinaryReversal(str) take the str parameter being passed, which will be 
#a positive integer, take its binary representation (padded to the nearest N * 8 bits), 
#reverse that string of bits, and then finally return the new reversed string in decimal 
#form. For example: if str is "47" then the binary version of this integer is 101111 but 
#we pad it to be 00101111. Your program should reverse this binary string which then 
#becomes: 11110100 and then finally return the decimal version of this string, which 
#is 244.
#Examples
#Input: "213"
#Output: 171
#Input: "4567"
#Output: 60296

def reverseBits(num,bitSize): 
     binary = bin(num) 
     reverse = binary[-1:1:-1] 
     reverse = reverse + (bitSize - len(reverse))*'0'
  
     # converts reversed binary string into integer 
     print(int(reverse,2))
  
# Driver program 
if __name__ == "__main__": 
    num = 1
    bitSize = 32
    reverseBits(num,bitSize) 



def BinaryReversal(bi):
    decimaltobinary = bin(bi)
    print(decimaltobinary)
    return decimaltobinary

BinaryReversal(4)

