if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command = input()
        if command.startswith('insert'):
            _, index, num = command.split(' ')
            arr.insert(int(index), int(num))
        elif command.startswith('remove'):
            _, value = command.split(' ')
            arr.remove(int(value))
        elif command.startswith('append'):
            _, value = command.split(' ')
            arr.append(int(value))
        elif command == 'print':
            print(arr)
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()