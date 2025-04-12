a = 5
b = 2
def number (a, b):
    return a + b
result = number(a, b)
print(result)

def even_odd (number):
    if number % 2 == 0:
        return"even"
    else:
        return"odd"
result1 = even_odd (a)
result2 = even_odd (b)
print(result1)
print(result2)