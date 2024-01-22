def task1():
    number = int(input())
    print(f"{'Even' if number % 2 == 0 else 'Odd'}")

def task2():
    number = input()
    res = (int(number[0]) + int(number[3]) == int(number[1]) - int(number[2]))
    print(f"{'YES' if res else 'NO'}")

def task3():
    age = int(input())
    print(f"{'Access alowed' if age > 18 else 'Access denied'}")

def task4():
    numbers = list(map(int, input().split()))
    if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
        print("YES")
    else:
        print("NO")

def task5():
    a, b = map(int, input().split())
    print(min(a, b))

def task6():
    a, b, c, d = list(map(int, input().split()))
    print(min(a, min(b, min(c, d))))

def task7():
    age = int(input())
    if age <= 13:
        print("Childhood")
    elif age <= 24:
        print("Youth")
    elif age <= 59:
        print("Maturity")
    else:
        print("Old age")

def task8():
    numbers = list(map(int, input().split()))
    sum = 0
    for num in numbers:
        if num > 0:
           sum += num
    print(sum)

def task9():
    x = int(input())
    print(f"{'Yes' if -1 < x < 17 else 'No'}")

def task10():
    x = int(input())
    print(f"{'yes' if -3 <= x <= 7 else 'No'}")

def task11():
    number = int(input())
    if len(str(number)) == 4 and (number % 7 == 0 or number % 17 == 0):
        print("YES")
    else:
        print("NO")

def task12():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("YES")
    else:
        print("NO")

def task13():
    fx, fy = map(int, input().split())
    sx, sy = map(int, input().split())
    print(f"{'Yes' if (fx == sx or fy == sy) and sx != sy else 'No'}")

def task14():
    fx, fy = map(int, input().split())
    sx, sy = map(int, input().split())
    print(f"{ 'YES' if (abs(fx - sx) < 2 and abs(fy - sy) < 2) else 'No'}")

