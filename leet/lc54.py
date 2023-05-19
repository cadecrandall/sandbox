import array
import bisect
from typing import List
from icecream import ic

"""
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    output_list = []

    m = len(matrix)
    n = len(matrix[0])
    ic(m, n)

    i = j = 0
    i_min = 0
    j_min = 0
    i_max = m 
    j_max = n

    direction_loop = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0

    while len(output_list) < m*n:
        output_list.append(matrix[i][j])
        matrix[i][j] = None
        delta_i, delta_j = direction_loop[direction_idx]
        ic(delta_i, delta_j)

        i_next, j_next = i + delta_i, j + delta_j
        if not i_min <= i_next < m or not j_min <= j_next < n or not matrix[i_next][j_next]:
            direction_idx = (direction_idx + 1) % 4
            delta_i, delta_j = direction_loop[direction_idx]
        
        i += delta_i
        j += delta_j

    return output_list

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder(matrix))
