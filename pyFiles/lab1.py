from math import *


def perimeter():
    side = int(input())
    print(f"P = 4*a = {side * 4}")
    print(f"S = a^2 = {side ** 2}")


def rectangle():
    a = int(input())
    b = int(input())
    print(f"S = a*b = {a * b}")
    print(f"P = 2(a + b) = {2 * (a + b)}")


def parallelepiped():
    a = int(input())
    b = int(input())
    c = int(input())
    print(f"V = a * b * c = {a * b * c}")
    print(f"S = 2(a*b + b*c + a*c) = {2 * (a * b + b * c + a * c)}")


def geometric():
    a = int(input())
    b = int(input())
    print(f"Geometric mean = sqrt(a * b) = {sqrt(a * b)}")


def rightTriangle():
    a = int(input())
    b = int(input())
    c = sqrt(a ** 2 + b ** 2)
    print(f"c = sqrt(a^2 + b^2 = {c}")
    print(f"P = a + b + c = {a + b + c}")


def changeValues():
    a = input()
    b = input()
    c = input()

    a, b, c = b, c, a
    print(f"New values:\na = {a}\nb = {b}\nc = {c}")


def changeVals():
    a = input()
    b = input()
    c = input()

    a, b, c = c, a, b
    print(f"New values:\na = {a}\nb = {b}\nc = {c}")


def func1():
    # y = 3x^6 - 6x^2 + 7
    x = int(input())
    print(f"y = {3 * pow(x, 6) - 6 * pow(x, 2) + 7}")


def func2():
    # y = 4(x - 3)^6 + 7(x - 2)^3 + 2
    x = int(input())
    print(f"y = {4 * pow((x - 3), 6) + 7 * pow((x - 2), 3) + 2}")


def sayHello():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


def sumOfDigits():
    strNum = input("Enter number: ")
    sum = 0
    for i in range(len(strNum)):
        sum += int(strNum[i])
    print(f"The sum of digits is {sum}")


# 12
def eqTime():
    seconds = int(input("Enter amount of seconds: "))
    minutes = 0
    hours = 0
    days = 0
    while seconds > 59:
        seconds -= 60
        minutes += 1
        if minutes >= 60:
            hours += 1
            minutes = 0
            if hours >= 24:
                days += 1
                hours = 0
    print(f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}")

def weekDay():
    k = int(input())
    day = k % 7
    if (day == 0):
        print("Monday")
    elif (day == 1):
        print("Tuesday")
    elif (day == 2):
        print("Wednesday")
    elif (day == 3):
        print("Thursday")
    elif (day == 4):
        print("Friday")
    elif (day == 5):
        print("Saturday")
    else:
        print("Sunday")


def sortNums():
    a, b, c = map(int, input().split())
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        c, b = b, c
    print(f"Sorted numbers are {a}, {b}, {c}")


def task15():
    a, b, c = map(int, input().split())
    print(f"The sum is {a + b + c}")
    print(f"The difference is {a - b - c}")
    print(f"The product is {a * b * c}")


def task16():
    a, b = map(int, input().split())
    print(f"{(abs(a) + abs(b)) / (1 + abs(a * b))}")


def cube():
    length = int(input("Enter the length of the cube: "))
    print(f"The area of the cube is: {length * length * length}")
    print(f"The are of its side surface: {length * length}")


def task18():
    first, second = map(int, input().split())
    print(f"The arithmetic mean of {first} and {second} is {(first + second) / 2}")
    print(f"The geometric mean of {first} and {second} is {sqrt(first * second)}")


def task19():
    x, y, z = map(int, input().split())
    a = (sqrt(abs(x - 1)) - (abs(y) ** 1 / 3)) / (1 + ((x * x) / 2) + ((y * y) / 4))
    b = x * (atan(z) + e ** (-(x + 3)))
    print(f"a = {a}")
    print(f"b = {b}")


def task20():
    x, y, z = map(int, input().split())
    a = (3 + e ** (y - 1)) / (1 + (x * x) * (abs(y - tan(z))))
    b = 1 + abs(y - x) + (pow((y - x), 2) / 2) + (pow((abs(y - x)), 3) / 3)
    print(f"a = {a}")
    print(f"b = {b}")


def task21():
    x, y, z = map(int, input().split())
    a = (1 + y) * (((x + y) / (x * x + 4)) / (e ** (0 - x - 2) + 1) / (x * x + 4))
    b = (1 + cos(y - 2)) / ((x ** 4) / 2 + sin(z) ** 2)

    print(f"a = {a}")
    print(f"b = {b}")


def task22():
    x, y, z = map(int, input().split())
    a = y + x / ((y ** 2) + abs(x ** 2 / (y + (x ** 3) / 3)))
    b = 1 + tan(z / 2) ** 2

    print(f"a = {a}")
    print(f"b = {b}")


def task23():
    x, y, z = map(int, input().split())
    a = (2 * cos((x - pi) / 6)) / (1 / 2 + sin(y) ** 2)
    b = (1 + z ** 2) / (3 + (z ** 2) / 5)

    print(f"a = {a}")
    print(f"b = {b}")


def task24():
    x, y, z = map(int, input().split())
    a = (1 + (sin(x + y) ** 2)) / (2 + abs((x - 2 * x) / (1 + ((x ** 2) * (y ** 2))))) + x
    b = cos(atan(1 / z)) ** 2

    print(f"a = {a}")
    print(f"b = {b}")


def task25():
    x, y, z = map(int, input().split())
    atemp = ((y - sqrt(abs(x))) * (x - (y / (z + (x ** 2) / 4))))
    a = log(atemp, e)
    b = x - ((x ** 2) / factorial(3)) + ((x ** 5) / factorial(5))

    print(f"a = {a}")
    print(f"b = {b}")


def task32():
    x1, y1 = map(int, input("Enter first point coordinates: ").split())
    x2, y2 = map(int, input("Enter second point coordinates: ").split())

    d = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    print(f"Distance between two points is {d}")


def calcDistance(first, second):
    return sqrt(((first[0] - second[0]) ** 2) + ((first[1] - second[1]) ** 2))


def triangle():
    a = list(map(int, input("Enter coordinates: ").strip().split()))
    b = list(map(int, input("Enter coordinates: ").strip().split()))
    c = list(map(int, input("Enter coordinates: ").strip().split()))

    perim = calcDistance(a, b) + calcDistance(b, c) + calcDistance(a, c)
    print(f"Perimeter is equal to {perim}")
