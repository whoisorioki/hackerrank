if __name__ == '__main__':
    people = {}
    N = int(input())
    for _ in range(N):
        name, number = input().split()
        number = int(number)
        people[name] = number

    while True: 
        try:
            person = input()
        except EOFError:
            break
        if person in people:
            print(f"{person}={people[person]}")
        else:
            print("Not found")