if __name__ == '__main__':
    people = {}
    for _ in range(int(input())):
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