class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = self.array.copy()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        return random.sample(self.array, len(self.array))
