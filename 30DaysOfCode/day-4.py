class Person:
    def __init__(self, initialAge):
        self.age = initialAge
        if self.age < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age > 12 and self.age < 18:
            print('You are a teenager.')
        elif self.age > 17:
            print('You are old.')

    def yearPasses(self):
        self.age += 1


t = int(input()) # 4 -1 10 16 18
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
