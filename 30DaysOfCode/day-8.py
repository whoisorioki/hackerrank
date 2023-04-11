if __name__ == '__main__':
    people = {}
    N = int(input())
    for _ in range(N):
        name, *line = input().split()
        number = list(map(int, line))
        number = number[0]
        people[name] = number

    for k, v in people.items(): 
        person = input()
        if person == k:
            print(f'{k}={v}')
        else:
            print('Not found')
