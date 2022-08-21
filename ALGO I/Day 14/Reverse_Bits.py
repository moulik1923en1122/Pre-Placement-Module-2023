class Solution:
    def reverseBits(self, n: int) -> int:

        q =  bin(n)[2:]        
        new_num = "".join(["0"]*(32-len(q))) + q 
        new_num = new_num[::-1]

        return int(new_num,2)