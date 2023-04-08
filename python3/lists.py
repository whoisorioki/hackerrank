if __name__ == '__main__':
    import sys
    N = int(input())

    array = []
    for _ in range(N):
        answer, *line = input().split()
        numbers = list(map(int, line))
        if answer == 'insert':
            array.insert(numbers[0], numbers[1])
        if answer == 'print':
            print(array)
        if answer == 'remove':
            array.remove(numbers[0])
        if answer == 'append':
            array.append(numbers[0])
        if answer == 'sort':
            array.sort(reverse=False)
        if answer == 'pop':
            array.pop()
        if answer == 'reverse':
            array.reverse()