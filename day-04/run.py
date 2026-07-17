# #check if the number is even or odd
# num = int(input(" enter the number  -  "))
# # if num %2 == 0:
# #     print("even")
# # else:
# #     print("odd")

# num2 = int(input(" enter the number  -  "))
# if num>num2:
#     print(f"num1 is greater {num1}")
# else:
#     print(f"num2 is greater {num2}")


#age 

# age = int(input("enter you age =="))
# if age>=18:
#     print("you can vote")
# else:
#     print("you cant vote")



# marks = int(input(" input you marks to check pass or fail"))
# if marks>=40:
#     print("pass")
# else:
#     print("fail")


#leap year
#rule 
#leap year is devided by 400 and 4 and 100 devide should be no 0 

# year = int(input(" enter you leap year ===    "))

# if (year%400==0 or (year%4==0 and year%100 !=0)):
#     print("leap year")
# else:
#     print("not a leap year")

# #check if the number is devided by 3 and 5 number
# num = int(input("enter num to check    =   "))
# if num%3==0 and num%5==0:
#     print("yes")
# else:
#     print("no")



# #username and pass checking
# username = input(" enter you username =")
# password = input(" enter you password")
# if username=="admin" and password =="admin123":
#     print("login sucessfull")
# else:
#     print("not logged in")


# #check if number is negetive,positve or zero

# num = int(input(" enter you num   =   "))
# # if num==0:
# #     print("zero")
# # elif num>0:
# #     print("positive")
# # else:
# #     print("negative")


# #greatest number of 3 number
# num2 = int(input(" enter the number  -  "))
# num3 = int(input(" enter the number  -  "))

# if num>num2 and num>num3:
#     print(f"num1 is gretest {num}")
# elif num2>num and num2>num3:
#     print(f"num2 {num2}")
# else:
#     print(f"num3 {num3}")

# #check vowel or any constant
# text = input("enter you text here ")
# if text in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("constant")


# taking marks from user and check the grade
# Print the grade:

# 90–100 → A+
# 80–89 → A
# 70–79 → B
# 60–69 → C
# 40–59 → D
# Below 40 → Fail
# marks = int(input(" enter you marks ==   "))
# if marks==0:
#     print("please input you real marks")
# elif marks>=90:
#     print("A+")
# elif marks>=80:
#     print("A")
# elif marks>=70:
#     print("B")
# elif marks>=60:
#     print("c")
# elif marks>=40:
#     print("d")
# else:
#     print("fail")

#check the how is oldest among 3 people


# age1 = int(input("enter you age"))

# age2 = int(input("enter you age"))

# age3 = int(input("enter you age"))
# if age1>age2 and age1>age3:
#     print("age1 is oldest")
# elif age2>age1 and age2>age3:
#     print("age 2 oldest")
# else:
#     print("age3 oldest")


#give loan if age is 21 and income at least a50000

age1 = int(input("enter you age"))
income = int(input(" enter you income ==  "))
if age1>=21 and income>=50000:
    print("you can get loan")
else:
    print("sorry, no loan")