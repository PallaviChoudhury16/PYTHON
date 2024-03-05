# Write a program to enter a string and print it in reverse and also print the number of vowels and consonants in it.
vc = 0  
cc = 0  
s1 = input("Enter a string : ")
s1 = s1.lower()  
for i in range(0,len(s1)):   
    if s1[i] in ('a',"e","i","o","u"):  
        vc = vc + 1;  
    elif (s1[i] >= 'a' and s1[i] <= 'z'):  
        cc = cc + 1;  
print("Total number of vowels are ",vc)
print("Total number of consonants are ",cc)
print("Reverse of the string is ",s1[: :-1])
 
