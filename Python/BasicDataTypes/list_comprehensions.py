if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[x_i, y_i, z_i] for x_i in range(x+1) for y_i in range(y+1) for z_i in range(z+1) if x_i + y_i + z_i != n])
