from typing import List
from icecream import ic



def findBall(grid: List[List[int]]) -> List[int]:
    # to the right: 1
    # to the left : -1
    
    # stuck if it hits a V, return -1
    # run through each of the i columns
    
    nrows = len(grid)
    ncols = len(grid[0])

    def h(r, c):
        # make recursive call
        print(f'Recursive call at ({r}, {c})')
        
        if r == nrows:
            return c

        c_next = c + grid[r][c]
        r_next = r + 1

        if c_next < 0 or c_next >= ncols:
            # stuck against the wall
            return -1

        if grid[r][c_next] == grid[r][c]:
            return h(r_next, c_next)
        else:
            return -1

    
    answers = [-1 for i in range(ncols)]
    
    for i in range(ncols):
        # simulate the ith column
        print(f'Starting column {i} at (0, {i})')
        answers[i] = h(0, i)
        ic(answers)
    return answers


if __name__ == '__main__':
    grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    grid2 = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

    grid1_ans = findBall(grid)
    grid2_ans = findBall(grid2)

    print(f'Grid 1 (5x5) Correct: {grid1_ans == [1,-1,-1,-1,-1]}')
    print(f'Grid 2 (6x4) Correct: {grid2_ans == [0, 1, 2, 3, 4,-1]}')