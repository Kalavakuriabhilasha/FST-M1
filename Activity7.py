

x = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in x.split(" ")]
sum_of_list = sum(numbers)
print("The sum of the list is:", sum_of_list)
