import os
        

def queensAttack(n, k, r_q, c_q, obstacles):
    num_moves = 0
    directions = [[0, 1], [1, 0], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
    
    for d_x, d_y in directions:
        x, y = r_q + d_x, c_q + d_y
        while x >= 1 and y >= 1 and x <= n and y <= n:
            if [x, y] in obstacles:
                break
            num_moves += 1
            x += d_x
            y += d_y
    
    return num_moves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
