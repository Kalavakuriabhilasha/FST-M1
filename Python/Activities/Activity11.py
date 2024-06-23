
fruits = {
    "apple": 1.00,
    "banana": 0.50,
    "mango": 2.00,
    "orange": 1.50,
    "grape": 3.00,
    "watermelon": 4.00
}
fruit_to_check = input("Enter a fruit to check its availability: ")
if fruit_to_check.lower() in fruits:
    print(f"{fruit_to_check} is available.")
else:
    print(f"{fruit_to_check} is not available.")
