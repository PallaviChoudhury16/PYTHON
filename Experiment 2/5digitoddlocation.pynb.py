# Write a program to enter a 5 digit number and print the digits present at odd locations.
num = input("Enter a five digit number : ")
for i in range(len(num)):
    if(i % 2 == 0):
        print(num[i])
    i = i +1
    
