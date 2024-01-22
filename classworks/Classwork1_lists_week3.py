def task1():
    numbers = [(i + 1) for i in range(int(input()))]
    print(numbers)

def task2():
    n = int(input())
    chars = [chr(i) for i in range(97, 97 + n)]
    print(chars)

def task3():
    numbers1 = [1, 2, 3]
    numbers2 = [6]
    numbers3 = [7, 8, 9, 10, 11, 12, 13]
    print(numbers1 + numbers1 + (numbers2*9) + numbers3)

def task4():
    n = int(input())
    numbers = [int(input()) for i in range(n)]
    numbers = numbers[::2]
    print(numbers)

def task5():
    n = int(input())
    strings = [input() for i in range(n)]
    k = int(input())
    for string in strings:
        print(string[k - 1], end="")

def task6():
    n = int(input())
    strings = [input() for i in range(n)]
    chars = []
    for string in strings:
        for char in string:
            chars.append(char)

    print(chars)

def task7():
    n = int(input())
    inputs = [input().lower() for i in range(n)]
    k = int(input())
    searches = [input().lower() for i in range(k)]

    results = []

    for string in inputs:
        for i in range(k):
            if searches[i] not in string:
                continue
            if i == (k - 1):
                results.append(string)

    print(results)


def task8():
    numbers = [int(input()) for i in range(int(input()))]
    for number in numbers:
        if number < 0:
            print(number)
    for number in numbers:
        if number == 0:
            print(number)
    for number in numbers:
        if number > 0:
            print(number)


