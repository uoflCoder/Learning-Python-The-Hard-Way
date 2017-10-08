#Exercise 33

i = 0
numbers = []

while i < 6:
    print(f"At the top is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now:",numbers)
    print(f"At the bottom is {i}")

    print("The numbers:")
    for num in numbers:
        print(num)
