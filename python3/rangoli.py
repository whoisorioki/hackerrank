def print_rangoli(size):
    import string

    if size <= 0:
        print("Size should be a positive integer.")
        return

    alphabet = string.ascii_lowercase[:size]  # Get the alphabet characters up to size
    width = 4 * size - 3  # Calculate the width of the rangoli

    # Print the upper part of the rangoli
    for i in range(size - 1, -size, -1):
        row = '-'.join(alphabet[size - 1:abs(i):-1] + alphabet[abs(i):size])
        print(row.center(width, '-'))

    # Print the lower part of the rangoli
    for i in range(1, size):
        row = '-'.join(alphabet[size - 1:abs(i):-1] + alphabet[abs(i):size])
        print(row.center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
