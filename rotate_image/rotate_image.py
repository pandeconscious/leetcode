class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            n = len(matrix[0])
            if n > 1:
                for r in xrange(n/2):
                    for i in xrange(r, n-r-1):
                        t = matrix[r][i]
                        matrix[r][i] = matrix[n-i-1][r]
                        matrix[n-i-1][r] = matrix[n-r-1][n-i-1]
                        matrix[n-r-1][n-i-1] = matrix[i][n-r-1]
                        matrix[i][n-r-1] = t
