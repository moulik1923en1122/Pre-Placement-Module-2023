class Solution:
    def numDecodings(self, s: str) -> int:

        memo = dict()

        def getDecodings(index, s):

            if index in memo:
                return memo[index]

            # If got to the end of the string return 1
            if index == len(s):
                return 1

            # If 0, cannot decode (1 - 26 only A-Z)
            if s[index] == "0":
                return 0

            if index == len(s) - 1:
                return 1

            answer = getDecodings(index + 1, s) 


            # Double digit
            if int(s[index: index+2]) <= 26:
                answer += getDecodings(index + 2, s)

            memo[index] = answer
            return answer
        return getDecodings(0, s)