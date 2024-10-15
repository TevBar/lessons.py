#question2 task 1 number showdown 

num1= int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
if num2 >= num1 and num2 >= num3:
    largest = num2
else: 
    largest = num3


print(f"The largest number is:{largest}")

# what is the smallest number ? 

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"the smallest number is:{smallest}")