if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    f = max(arr)

    # arr1 = [i for i in arr if  i < f]
    arr1 = []
    for i in arr:
        if i < f:
            arr1.append(i)

    print(max(arr1))
