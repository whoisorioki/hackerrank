def split_and_join(line):
    sentence = line.split(' ')
    sentence = '-'.join(sentence)
    return sentence


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
