a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus → 1
print(a ** b)  # Exponent → 1000
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True
a = 5
b = 10

print(a < 10 and b > 5)   # True
print(a < 10 or b < 5)    # True
print(not(a < 10))        # False
x = 10
x += 5   # same as x = x + 5
x -= 2   # same as x = x - 2
x *= 3   # same as x = x * 3
x /= 2   # same as x = x / 2
print(x)
text = "Python"

print(text[0])      # P
print(text[-1])     # n
print(text[0:3])    # Pyt
print(text[2:])     # thon
print(text[:4])     # Pyth
print(text[::-1])   # nohtyP (reversed)
first = "Hello"
second = "World"
result = first + " " + second
print(result)   # Hello World
s = "  I love Python  "

print(s.upper())     # I LOVE PYTHON
print(s.lower())     # i love python
print(s.strip())     # removes extra spaces → "I love Python"
print(s.split())     # ['I', 'love', 'Python']
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
text = input("Enter a string: ")
print("Reversed:", text[::-1])
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print("Result:", a + b)
elif operator == '-':
    print("Result:", a - b)
elif operator == '*':
    print("Result:", a * b)
elif operator == '/':
    print("Result:", a / b)
else:
    print("Invalid operator!")

