example_set = {1,2,3,4,5}
print(example_set)
set_a = {1,2,3,}
set_b = {3,4,5}
union = set_a.union(set_b)
print(union)
print(set_a.intersection(set_b))
difference = set_a.difference(set_b)
print(difference)
example_set.add(10)
print(example_set)
#example_set.remove(2) #remove and discard works same.
example_set.discard(2)
print(example_set)