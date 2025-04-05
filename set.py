# set will not allow duplicte values

new_set = {1,2,2,3,2,7,5}
print(new_set)


# add values in set 

new_set.add(10)
print(new_set)

#  add the values in a to b

a = {1,2,3,}
b = {4,2,7}

a.update(b)
print(a)
b.update(a)
print(b)

print(a.union(b))
print(a.intersection_update(b))
print(a.intersection(b))
print(a.isdisjoint(b))