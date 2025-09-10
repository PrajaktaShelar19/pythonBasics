def hello_world():
    print("Hello World..!")
hello_world()

def greet(name,age):
    print(f"Hello {name}, you are {age} years old !")
greet("John", 25)

def sum_of_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
        print(f"The sum of {number} is {total}")
sum_of_numbers(2, 3, 4)
sum_of_numbers(1,2, 3,4,5)

def display_info(name, age, city="unknown"):
    print(f"Hello {name}, you are {age} years old!, city is {city}")

display_info("John", 25)
display_info("Prajakta", 31, "Pune")

def display_fruits(fruitList):
    for fruit in fruitList:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
display_fruits(my_fruits)

def multiple(a, b):
    result = a * b
    print(f"The result of {a} * {b} is {result}")

multiple(3,4)

def multiply(a, b):
    result2 = a * b
    return result2

result1= multiply(5, 4)
print(result1)

def calculate(a ,b):
    sum = a + b
    diff = a - b
    return sum, diff

result_sum, result_diff = calculate(7, 3)
print(f" The result of sum: {result_sum}, The result of diff: {result_diff}")

