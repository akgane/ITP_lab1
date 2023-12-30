import math
def cond1():
    number = int(input())
    if number > 0:
        number += 1
    elif number < 0:
        number -= 2
    else:
        number = 10
    print(number)

def cond2():
    numbers = [0, 0]
    for i in range(3):
        if int(input()) < 0:
            numbers[0] += 1
        else:
            numbers[1] += 1

    print(f"Number of negative: {numbers[0]}\nNumber of positive: {numbers[1]}")

def cond3():
    numbers = sorted(list(map(int, input().split())))
    print(numbers[1] + numbers[2])

def cond4():
    number = int(input())
    print(f"Number is {'even' if number % 2 == 0 else 'odd'}")

def cond5():
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        print("I")
    elif x > 0 and y < 0:
        print("II")
    elif x < 0 and y < 0:
        print("III")
    else:
        print("IV")

def loops1():
    a, b = map(int, input().split())
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print(sum)

def loops2():
    a, b = map(int, input().split())
    product = 1
    for i in range(a, b + 1):
        product *= i
    print(product)

def loops3():
    n = int(input())
    result = 0
    for i in range(n, (2 * n) + 1):
        result += i**2
    print(result)

def loops4():
    a = int(input())
    n = int(input())
    for i in range(1, n + 1):
        print(a ** i)

def loops5():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += math.factorial(i)
    print(sum)

