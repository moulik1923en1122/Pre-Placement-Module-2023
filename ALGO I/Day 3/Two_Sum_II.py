class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_i = 0
        end_i = len(numbers) - 1
        result = numbers[start_i] + numbers[end_i]
        
        while result != target:
            if result > target:
                end_i -= 1
            elif result < target:
                start_i += 1

            result = numbers[start_i] + numbers[end_i]

        return start_i + 1, end_i + 1