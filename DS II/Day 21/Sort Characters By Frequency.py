class Solution:
    def frequencySort(self, s: str) -> str:
        output = []
        for letter in set(s):
            count = s.count(letter)
            output.append(letter*count)
        output = sorted(output, key=len, reverse = True)
        return "".join(output)
        