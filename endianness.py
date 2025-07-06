#1.2.10 Exercises
# 1.Endianness
#Write a function int_to_little_endian(n, length) that converts any positive integer to a little-endian byte sequence of fixed length.

def int_to_little_endian(n, length):
    result = []
    for _ in range(length):
        result.append(n & 0xFF) #This extracts the least significant byte (LSB) from the integer n
        n >>= 8 #shifts right by 8 bits
    return bytes(result)

#test
n = 1000
ans = int_to_little_endian(n, 8)
print(ans)

#explanation
#we use the simple boolena algebra to find the little endian version
#first, we use the n & 0xFF. the 0xFF is a mask that is 00000000 11111111. we know that every 8 bits = 1 byte
#so we used this mask the get the LSB. 
#in the given example, 1000 int to binary is 00000011 11101000  => two bytes: high byte = 0x03, low byte = 0xE8
#so if we AND this with the mask, we easily get the low byte, leaving the high byte
#after we extracted the low byte, we extract the high byte by shifting to the right by 8 bits