import textwrap


def wrap(string, max_width):
    string = textwrap.wrap(text=string, width=max_width)
    new_string = ''
    for item in string:
        new_string += item + '\n'
    return new_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
