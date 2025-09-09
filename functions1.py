def calculate_average(*numbers):
    numbers = [10, 15, 20, 25, 30]
    average = sum(numbers)/len(numbers)
    return average

result = calculate_average(10,15,20,25,30)
print(f"the result of average is {result}")

def calculate_average1(numbers_cal):
    total = 0
    for number in numbers_cal:
        total += number
    average = total / len(numbers_cal)
    return average

numbers_cal = [10,15,20,25,30]

result1 = calculate_average1(numbers_cal)
print(f"the result of average is {result1}")
