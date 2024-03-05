## Write a program to enter 5 number and check the length

num=input("enter a five digit number: ")
for i in range(len(num)):
    if(i%2==0):
        print(num[i])
    i=i+1
