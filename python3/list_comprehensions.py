if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    d = list([a, b, c] for a in range(x + 1)
             for b in range(y + 1) for c in range(z + 1))

    e = list(i for i in d if sum(i) != n)

    print(e)