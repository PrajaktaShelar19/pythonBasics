customer_age = 45
time = 1600
base_ticketPrice = 12

if customer_age <= 12:
    discount = 0.5
elif customer_age >= 60:
    discount = 0.3
elif time < 1700:
    discount = 0.2
else:
    discount = 0

final_price = base_ticketPrice * (1- discount)
print(f"The final ticket price is: ${final_price:.2f}")