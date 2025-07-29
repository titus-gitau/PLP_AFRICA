#Basic calculator program
#Input
first_number = float(input("Enter the first number: "))

second_number = float(input("Enter the second  number: "))

#operations 

sum = first_number + second_number

difference_one = first_number - second_number
difference_two = second_number - first_number

product = first_number * second_number

division = first_number / second_number

floor_division = first_number // second_number

modulus = first_number % second_number


#output 
print(f"\nThe sum of {first_number} and {second_number} is {sum}\n")
print(f"The difference between {first_number} and {second_number} is {difference_one}\n")
print(f"The difference between {second_number} and {first_number} is {difference_two}\n")

print(f"The result of the product between {first_number} and {second_number} is {product}\n")

print(f"The result of division between {first_number} and {second_number} is {division}\n")

print(f"The result of the floor division between {first_number} and {second_number} is {floor_division}\n")

print(f"The result of modulus between {first_number} and {second_number} is {modulus}\n")