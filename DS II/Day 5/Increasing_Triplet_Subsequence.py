class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack=[]
        k=3
        for n in nums:
            if not stack or stack[-1]<n:
                stack.append(n)
                if len(stack)==k:
                    return True
            else:
                for i in range(len(stack)):
                    if stack[i]>=n:
                        stack[i]=n
                        break
        return False