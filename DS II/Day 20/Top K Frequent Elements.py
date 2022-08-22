class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
      
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        
        arr = []
        for i in range(len(nums) + 1):
            arr.append([])
     
        
        for num, count in count.items():
            arr[count].append(num)
            
        popped = 0
        j = len(arr) - 1
        while popped != k:
            if len(arr[j]) > 0:
                res += [arr[j].pop()]
                popped += 1
            if popped == k:
                break
            if len(arr[j]) == 0:
                j -= 1
        return res