#1 Sum
numbers = [1,2,3,4]
print(sum(numbers))

#2 Largest
numbers = [2,4,6]
print(max(numbers))

#3 Smallest
numbers = [2,4,6]
print(min(numbers))

#5 Prositive
numbers = [-4,-3,-2,-1,0,1,2,3]

positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
print(positive_numbers)

#7 Multiply
numbers = [1,2,3]
factor = 9

multiplied_numbers = []

for number in numbers:
    new_number = number * factor
    multiplied_numbers.append(new_number)
print(multiplied_numbers)

#8 Reverse String
numbers = [1,2,3]
factor = 9

multiplied_numbers = []

for number in numbers:
    new_number = number * factor
    multiplied_numbers.append(new_number)
print(numbers)
 
numbers.reverse()
print(numbers)