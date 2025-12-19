print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("Enter 1 or 2")

ch = int(input())

if ch == 1:
    f = float(input())
    c = (f - 32) * 5 / 9
    print(c)
elif ch == 2:
    c = float(input())
    f = (c * 9 / 5) + 32
    print(f)
else:
    print("Invalid Choice")
