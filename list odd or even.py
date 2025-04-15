def categorize_numbers(a):
    even_int = []
    odd_int = []
    if a % 2 == 0:
        even_int.append(a)
    else:
        odd_int.append(a)
    return even_int, odd_int

# Getting a list of numbers from the user
given_list = input("Enter the given numbers (space-separated): ").split()
given_list = [int(i) for i in given_list]  # Convert the input to integers

even_ints = []
odd_ints = []

# Iterating through the given list and categorizing numbers
for number in given_list:
    even, odd = ca