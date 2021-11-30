score = float(input("Enter your score : "))
MaxC = 100
grade = ["A","B","C","D","F"]
if score>=MaxC-10:
    print(f"Grade : {grade[0]}")
elif score>=MaxC-20 :
    print(f"Grade : {grade[1]}")
elif score>=MaxC-30 :
    print(f"Grade : {grade[2]}")
elif score>=MaxC-40 :
    print(f"Grade : {grade[3]}")
elif score<MaxC-10 :
    print(f"Grade : {grade[4]}")
else :
    print("your score was wrong type again")