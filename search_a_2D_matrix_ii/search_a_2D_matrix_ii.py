class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            if not matrix[0]:
                return False
            m, n = len(matrix), len(matrix[0])
            r, c = 0, n-1
            
            while r < m and c >= 0:
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    c -= 1
                else:
                    r += 1
            
            while r < m:
                if matrix[r][0] == target:
                    return True
                r += 1
            
            while c >= 0:
                if matrix[m-1][c] == target:
                    return True
                c -= 1
            
            return False
        return False
        
