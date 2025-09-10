n = 25
sum_total_numbers = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
      #  print(i)
        sum_total_numbers += i
print(f"sum of multiple of 3 and 5 up to {n} is: {sum_total_numbers}")

sum_of_while_loop = 0
current_number = 1
while current_number < n:
    if current_number % 3 == 0 or current_number % 5 == 0:
        sum_of_while_loop += current_number
    current_number += 1
print(f"sum of multiple of 3 and 5 up to {n} is: {sum_of_while_loop}")


