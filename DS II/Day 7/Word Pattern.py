class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return [*map(s.split(' ').index, s.split(' '))] == [*map(pattern.index, pattern)]