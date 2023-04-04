if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = []
    for student in students:
        scores.append(student[1])

    lowest = min(scores)

    scores1 = [score for score in scores if score > lowest]

    second = min(scores1)

    seconds = []
    for student in students:
        if student[1] == second:
            seconds.append(student[0])

    seconds.sort()
    for second in seconds:
        print(second)
