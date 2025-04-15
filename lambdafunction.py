square = lambda a: a * a
print(square(8))


# map of lambda function it will execute the all the elements in the function

my_list = [1,2,3,5,9]
square1 = lambda a: a * a * a
result = list(map(square1, my_list))
print(result)

#  filter of lambda function it will execute particular function is true or not

evens = set(filter(lambda a: a % 2 == 0, my_list))
print(evens)

# sort lambda function it will execute particular index from the list

num_list = [(1,4,7,"q"),(3,5,6,"g"),(3,56,4,"t")]
result3 = sorted(num_list)
# reverse the list in desending order
result3 = sorted(num_list, key=lambda a: a[3] ,reverse=True)
result4 = sorted(num_list, key=lambda a: a[3] ,reverse=False)
print(result3)
print(result4)