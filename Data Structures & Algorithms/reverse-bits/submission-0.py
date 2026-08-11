class Solution:
    def reverseBits(self, n: int) -> int:
        strN =  str(bin(n))[2:]
        n = 0
        c = 0
        length = len(strN)
        for i in range(32):
            if i < 32-length:
                n += 0
            else:
                n += (2**(i))*int(strN[c])
                c+=1
        return n
     