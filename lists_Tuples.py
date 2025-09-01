empty_list = []
print(empty_list)

My_List = [1,2, "Apple",3.14,4]
print(My_List)
print(len(My_List))
print(My_List[0])

#starts with index 1 as 2 and last index 4 is not included
sliced_List = My_List[1:4]
print("after sLice: " +str(sliced_List))

#replace 3 index in my list and print
My_List[2] = "Banana"
print("updated list: " +str(My_List))
print("length of mylist: " + str(len(My_List)))

#adds value
My_List.append('10')
print("Append:- " + str(My_List))

#adds another list
My_List.extend(['13',"Banana"])
print("extend:- " + str(My_List))

#insert into list
My_List.insert(0,'zero')
print("Insert:- " + str(My_List))

#count
print("banana count: " + str(My_List.count('Banana')))

empty_tuple = ()
print(empty_tuple)

my_tuple = (1,2, "Apple",3.14,4)
print(my_tuple)
print("-----my tuple methods--------------")
print(my_tuple[2])
print(my_tuple[1:4])
print(len(my_tuple))
print(my_tuple.count('Apple'))
print(my_tuple.index('Apple'))

#difference between List and tuple

