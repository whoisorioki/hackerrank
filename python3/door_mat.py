num1, num2 = map(int, input().split())
x = '.|.'
for i in range((num1 - 1) // 2):
    print((x * (i) + x * (i + 1)).center(num2, '-'))

print('WELCOME'.center(num2, '-'))

for i in range((num1 - 1) // 2):
    print((x * ((num1 - 2) - i * 2)).center(num2, '-'))