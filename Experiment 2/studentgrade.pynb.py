# Write a program to enter a percentage and display the gradation system.
per = float(input("Enter your percentage : "))
if per>=91 and per<=100:
    print("Your Grade is O")
elif per>=81 and per<91:
    print("Your Grade is E")
elif per>=71 and per<81:
    print("Your Grade is A")
elif per>=61 and per<71:
    print("Your Grade is B")
elif per>=51 and per<61:
    print("Your Grade is C")
elif per>=41 and per<51:
    print("Your Grade is D")
elif per>=33 and per<41:
    print("Your Grade is F")
else:
    print("Invalid Input!")
