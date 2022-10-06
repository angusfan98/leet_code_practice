'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''


def searchMatrix(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    r = 0
    l = m*n-1

    if m == 0:
        return False
    
    while r <= l:
        mid = (r+l)//2
        cur = matrix[mid//n][mid%n]
        print(cur)
        if cur == target:
            return True
        elif target > cur:
            r = mid + 1
        else:
            l = mid - 1
    return False


target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(searchMatrix(matrix,target))
