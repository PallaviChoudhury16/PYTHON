# Write a program to enter a number and check whether it is a palindrome number or not.
num = int(input("Enter a number : "))
p = num
sum = 0
while(num > 0):
    d = num % 10
    sum = (sum * 10) + d
    num = num // 10
if(p == sum):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
