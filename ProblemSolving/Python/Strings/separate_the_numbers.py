def validate_sequence(s, first_number):
    while s:
        if s.startswith(first_number):
            s = s[len(first_number):]
            first_number = str(int(first_number) + 1)
        else:
            return False
    return True


def separateNumbers(s):
    if s[0] == '0' and len(s) > 1:
        print('NO')
        return

    for i in range(1, int(len(s) / 2) + 1):
        if validate_sequence(s, s[:i]):
            print(f'YES {s[:i]}')
            return
    print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
