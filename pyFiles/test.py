from math import sqrt


def task0():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")

def task1():
    print(15 + 50)
    print(31 + 34)
    print(52 + 13)
    print(17 + 48)
    print(5 * 13)
    print(130 / 2)

def task2():
    print(7.025 * 10)
    print(1.5 * 281 / 6)
    print(32.125 + 38.125)
    print(123.153 - 52.903)
    print(70 + (0.5 ** 2))

def task3():
    #print(type(3 + 1.5 + 4))
    print("float")

def task4():
    number = int(input("Enter number: "))
    print("Square root of " + str(number) + " is (sqrt(number)): " + str(sqrt(number)))
    print("Square of " + str(number) + "is (number ** 2): " + str(number**2))

def task5():
    #print(100 % 7)
    print(2)

def task6():
    print(7 ** 3)

def task7():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    print("Sum: " + str(first + second))
    print("Difference: " + str(first - second))
    print("Multiplication: " + str(first * second))

def task8():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    print("Integer division: " + str(int(first / second)))
    print("Float division: " + str(float(first) / float(second)))

def task9():
    numbers = [4, 8, 15, 16, 23, 42]
    for number in numbers:
        print(number, end=' ')

def task10():
    numbers = [4, 8, 15, 16, 23, 42]
    for number in numbers:
        print(number)

def task11():
    count = int(input("Enter number of asterisks: "))
    counter = 1
    for i in range(count):
        print('*' * counter)
        counter += 1

def task12():
    name = input("Enter your name: ")
    print("Hello, " + name)

def task13():
    team = input("Enter team name: ")
    print(team + " - champion!")

def task14():
    inputs = []
    for i in range(3):
        inputs.append(input())
    for inp in inputs:
        print(inp)

def task15():
    inputs = []
    for i in range(3):
        inputs.insert(0, input())
    for inp in inputs:
        print(inp)

def task16():
    print("I", "like", "Python", sep="***")

def task17():
    separator = input()
    inputs = []
    for i in range(3):
        inputs.append(input())
    print(inputs[0], inputs[1], inputs[2], sep=separator)

def task18():
    number = int(input())
    for i in range(3):
        print(number)
        number += 1

def task19():
    numbers = []
    for i in range(3):
        numbers.append(int(input()))
    print(sum(numbers))

def task20():
    number = int(input())
    results = [number * i for i in range(1, 6)]
    print(results[0], results[1], results[2], results[3], results[4], sep='---')

def task21():
    a1 = int(input())
    d = int(input())
    n = int(input())
    print(a1 + (n - 1) * d)

def task22():
    first = int(input())
    second = int(input())
    print(str(first) + " + " + str(second) + " = " + str(first + second))
    print(str(first) + " - " + str(second) + " = " + str(first - second))
    print(str(first) + " * " + str(second) + " = " + str(first * second))

def task23():
    number = int(input())
    print(f"The next number after {number} is: {number + 1}")
    print(f"For the number {number} the previous number is: {number - 1}")

def task24():
    kids = int(input())
    tangerines = int(input())

    print("Every student got: " + str(tangerines // kids))
    print(str(tangerines % kids) + " tangerines remain in basket")

def task25():
    number = input()
    digits = [int(number[i]) for i in range(3)]
    print("Sum if digits: " + str(sum(digits)))
    prod = digits[0] * digits[1] * digits[2]
    print("Product of digits: " + str(prod))

task25()