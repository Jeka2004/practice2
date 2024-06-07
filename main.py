# Завдання 1
a = 10
b = 5

# Завдання 2
expression1 = (a > b) and (a > 0)
expression2 = (a != b) and (b > 0)

expression3 = (a < b) and (b > 0)
expression4 = (a == b) and (a < 0)

print(f"Expression1: {expression1}")
print(f"Expression2: {expression2}")
print(f"Expression3: {expression3}")
print(f"Expression4: {expression4}")

# Завдання 3
expression5 = (a > b) or (a < 0)
expression6 = (a != b) or (b < 0)

expression7 = (a < b) or (a == 0)
expression8 = (a == b) or (b < 0)

print(f"Expression5: {expression5}")
print(f"Expression6: {expression6}")
print(f"Expression7: {expression7}")
print(f"Expression8: {expression8}")

# Завдання 4
string1 = "Hello"
string2 = "World"

# Істина
expression9 = (len(string1) > len(string2)) and ("H" in string1)
expression10 = (string1 != string2) and (string2.startswith("W"))

# Хибність
expression11 = (len(string1) < len(string2)) and ("Z" in string1)
expression12 = (string1 == string2) and (string2.endswith("d"))

print(f"Expression9: {expression9}")
print(f"Expression10: {expression10}")
print(f"Expression11: {expression11}")
print(f"Expression12: {expression12}")

# Завдання 5
x = 5

if x > 0:
    print("Змінна x більше 0")
else:
    print("Змінна x менше або дорівнює 0")

x = -3

if x > 0:
    print("Змінна x більше 0")
else:
    print("Змінна x менше або дорівнює 0")

# Завдання 6
x = 5

if x > 0:
    print(1)
else:
    print(-1)

x = -3

if x > 0:
    print(1)
else:
    print(-1)

# Завдання 7
a = 10
b = 5

if a > b:
    c = a - b
elif a < b:
    c = a + b
else:
    c = a

print("Значення третьої змінної c:", c)

# Завдання 8

def compute_y(x):
    if -2.4 <= x <= 5.7:
        return x**2 / 4
    else:
        return 0

x = float(input("Enter a real number: "))
y = compute_y(x)
print(f"Y = {y}")
