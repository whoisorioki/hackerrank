if __name__ == '__main__':
    for _ in range(int(input())):
        letters = []
        name = input()
        for letter in name:
            letters.append(letter)
        for i in range(0, len(letters)):
            if i % 2 == 0:
                print(letters[i], end='')
        print(end=' ')
        for i in range(0, len(letters)):
            if i % 2 != 0:
                print(letters[i], end='')
        print()
