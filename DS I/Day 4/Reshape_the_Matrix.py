class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
            if len(mat) * len(mat[0]) != r * c:
                return mat
            result = []

            k = 0
            l = 0
            result.append([])
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if l >= c:
                        l = 0
                        k += 1
                        result.append([])
                    result[k].append(mat[i][j])
                    l += 1
            return result
            