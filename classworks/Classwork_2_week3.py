import random


def lnt1():
    fruits = list(input("Write favourite fruite: ") for i in range(5))


def lnt2():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums[2:7])


def lnt3():
    nums = tuple(int(input()) for i in range(3))
    print(nums)


def lnt4():
    nums = list(random.randrange(1, 100) for i in range(10))
    print(f"Initial list: {nums}")
    nums.append(int(input("Enter a number to add to the end: ")))
    nums.remove(nums[0])
    print(sorted(nums))


def lnt5():
    nums = list(random.randrange(1, 100) for i in range(20))
    print(nums)
    userInput = int(input("Enter a number to search: "))
    if userInput in nums:
        print("Number is in list")
    else:
        print("Number is not in list")


def lnt6():
    nums = list(random.randrange(1, 100) for i in range(20))
    print(nums)
    print(nums[::-1])


def lnt7():
    nums = list(random.randrange(1, 100) for i in range(4))
    a, b, c, d = nums[0], nums[1], nums[2], nums[3]
    print(a, b, c, d)


def lnt8():
    nums = list(int(input()) for i in range(10))
    print(f"Min number is {min(nums)}")
    print(f"Max number is {max(nums)}")


def lnt9():
    print("Enter 5 first elements: ", end="")
    first = list(input() for i in range(5))
    print("Enter 5 second elements: ", end="")
    second = list(input() for i in range(5))
    print(f"Concatenated list: {first + second}")


def lnt10():
    lst = list(int(input()) for i in range(5))
    print(tuple(lst))


def snd1():
    nums = set(list(int(input()) for i in range(5)))
    print(nums)


def snd2():
    mySet1 = set([random.randrange(1, 100) for i in range(5)])
    mySet2 = set([random.randrange(1, 100) for i in range(5)])
    print(f"Default set 1: {mySet1}")
    print(f"Default set 2: {mySet2}")
    print(f"Union is {mySet1.union(mySet2)}")
    print(f"Intersection is {mySet1.intersection(mySet2)}")
    print(f"Difference is {mySet1.difference(mySet2)}")
    print(f"Symmetric difference is {mySet1.symmetric_difference(mySet2)}")


def snd3():
    myDict = dict()
    for i in range(3):
        data = input("Enter key and value separated by a space: ").split(" ")
        myDict[data[0]] = data[1]
    print(f"Result dictionary: {myDict}")


def snd4():
    myDict = {"color": "red", "size": "medium", "price": 1000, "fruit": "apple"}
    key = input("Enter key: ")
    print(f"Value of key is {myDict[key]}" if key in myDict else f"There is no value by key")

def snd5():
    userInput = input("Enter some string: ")
    freq = dict()
    for char in userInput:
        if char.lower() not in freq:
            freq[char.lower()] = 1
        else:
            freq[char.lower()] += 1
    print(freq)

def snd6():
    my_set = set(random.randrange(1, 20) for i in range(10))
    #print(my_set)
    print("Number is in set" if int(input("Enter a number: ")) in my_set else "Number is not in set")

def snd7():
    my_dict = {"color": "red", "size": "medium", "price": 100, "fruit": "apple"}
    for key, value in my_dict.items():
        print(my_dict[key])

def snd8():
    first_dict = {"color": "red", "size": "medium", "price": 100, "fruit": "apple"}
    second_dict = {"university": "AITU", "language": "english", "country": "Kazakhstan", "name": "Akhan"}
    for key, value in first_dict.items():
        second_dict[key] = value
    print(second_dict)

def snd9():
    my_dict = {"color": "red", "size": "medium", "price": 100, "fruit": "apple"}
    print(f"Dictionary: {my_dict}")
    key = input("Enter key to remove from dictionary: ")
    del my_dict[key]
    print(f"Dictionary: {my_dict}")

def snd10():
    my_list = list(random.randrange(1, 11) for i in range(10))
    print(f"List: {my_list}")
    my_set = set(element for element in my_list if my_list.count(element) == 1)
    print(f"Set: {my_set}")

snd10()
