# Write a program to enter a number and check whether the number is perfect number or not
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if(num % i == 0):
        sum = sum + i
if (sum == num):
    print("It is a Perfect number")
else:
    print("It is not a Perfect number")
