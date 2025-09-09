x = 3
print(x)

y = x+5
print(y)

z = y/2
print(z)

x += 3
print(x)

x/=2
print(f"x = {x}")
x*=2
print(x)
x//=2
print(x)

print("-------------------")
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)

print("-------------------")
fruits = ["apple", "orange", "banana", "cherry"]
print("banana" in fruits)
print('mango' in fruits)
print("cherry" in fruits)
print("mango" not in fruits)

print(" ---------variables---------")
a = 5
b = 5
print(a==b)
print(a!=b)
print (a is b)

print(" ---------variables 1 ---------")
list_a = [1,3,5]
list_b = [1,3,5]
print(list_a == list_b)
print(list_a is list_b)  # false because different memory objects

print("==============================")
list_c = list_a
print(list_c is list_a)

list_d  = list_a.copy()
print(list_d is list_a)  # d will be the different object

