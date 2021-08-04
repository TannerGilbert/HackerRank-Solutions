import os
import copy


def cavityMap(grid):
    grid = [list(map(int, list(row))) for row in grid]
    updated_grid = copy.deepcopy(grid)
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            v = grid[i][j]
            if grid[i-1][j] < v and grid[i+1][j] < v and grid[i][j-1] < v and grid[i][j+1] < v:
                updated_grid[i][j] = 'X'

    return [''.join(list(map(str, row))) for row in updated_grid]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
