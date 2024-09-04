

x = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in x.split()]
if numbers[0] == numbers[-1]:
    print("True: The first and last number of the list are the same.")
else:
    print("False: The first and last number of the list are not the same.")
