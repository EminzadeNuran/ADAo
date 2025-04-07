# print("Hello world")

# float=5.5 number
# int=5 number
# str="hello" string
# list=[1,2,3,4,5] array
# dict={"a":1,"b":2} object
# tuple=(1,2,3,4,5) array
# set={1,2,3,4,5} array

# if,else,elif

# a=14
# b=15

# if a>b:
#     print("a>b")
# elif a<b:
#     print("a<b")
# else:
#     print("a=b")


# age = int(input("Enter your age: "))


# if age > 18:
#     print("Yasiniz catir")
# else:
#     print("Yasiniz catmir")

# print (type(age))

# format
# print(f"Yasiniz {age}")

# print (
#     """
#     """
# )

# ad = input("Adinizi daxil edin: ")
# yas = int(input("Yasinizi daxil edin: "))
# username = input("Username daxil edin: ")
# password = input("Password daxil edin: ")


# if yas > 18:
#     print("Yasiniz catir")
# else:
#  print(f"""
# Adiniz: {ad}
# Yasiniz: {yas}
# Username: {username}
# Password: {password}

# """)


# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))

# bmi = weight / height ** 2

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")

# in, not, range

# ad= ("Nuran Eminzada")

# if "a"  in ad:
#     print("True")
# else:
#     print("False")
    
    
#     if "a" not in ad:
#         print("True")
#     else:    
#         print("False")
#         # ters muhendislik
        
        
# while
# while logical operator

# a= 0

# while a < 100:
#     a+=1
#     print(a)

# a=0
# b=0
# ad= "Nuran Eminzada"

# while a < 10:
#     a+=1
#     b+=1
#     ad = input("Adinizi daxil edin: ")
#     print(ad)


# gauss = 0
# for i in range(1,101):
#     gauss += i
    
# print(gauss)


# for

# ad =    ("Nuran Eminzada")

# for j, i in enumerate(ad):
#     print(j, i)

# for i in range(1,101):
#     if i % 2 == 0:
#         print(f"Even: {i}")
#     else:
#         print(f"Odd:  {i}")

# FizzBuzz

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# for interval operator


# qiymet = int(input("Qiymeti daxil edin: "))

# if 90 <= qiymet and qiymet <= 100:
#     print("Ela")
# elif 70 <= qiymet and qiymet <= 89:
#     print("Yaxsi")
# elif 50 <= qiymet and qiymet <= 69:
#     print("Kafi")
# elif 0 <= qiymet and qiymet < 50:
#     print("Ugursuz")
# else:
#     print("Qiymet daxil edin")


# toplam = 0

# while True :
#     num =int(input("reqem yazin"))
#     if num < 0:
#         break
#     toplam += num
    
#     print("cem",toplam)

# correct_password = "1234"

# while True:
#     password = input("Kodu daxil edin")
#     if password == correct_password:
#         print("Kodunuz dogrudur")
#         break
#     print ("Kodunuz yanlisdi yeniden sinayin")    

# break, continue,yield

# liste= [1,2,3,4,5,6,7,8,9,10]
#  (editable)

# liste.append(36)
# print(liste)
# liste.pop()
# print(liste)
# liste.sort()
# print(liste)



#append, pop, remove, sort, index, count (list method)

# del, sum, min, max


# import random

# # randint

# reqem = random.randint(15,100)

# print(reqem)

# choice

# liste = [1,2,3,4,5,6,7,8,9,10]
# print(random.choice(liste))

# Task

# Computer choice
# User choice

# import random

# reqem = random.randint(0,101) 

# while True:
#     daxilolan_reqem = int(input("Reqemi daxil edin: "))
#     if daxilolan_reqem == reqem:
#         print("Tebrikler")
#         break
#     elif daxilolan_reqem > reqem:
#         print("isti")
#     else:
#         print("soyuq")
        

# Passworld Generation

# import random
# import string

# Password_length = int(input("Password uzunlugunu daxil edin: "))
# Password_letter_count = int(input("Password herf sayini daxil edin: "))
# Password_number_count = int(input("Password reqem sayini daxil edin: "))
# Password_symbol_count = int(input("Password simvol sayini daxil edin: "))

# password = ""

# for i in range(Password_letter_count):
#     password += random.choice(string.ascii_letters)

# for i in range(Password_number_count):
#     password += random.choice(string.digits)

# for i in range(Password_symbol_count):
#     password += random.choice(string.punctuation)
    

# password_list = list(password)
# random.shuffle(password_list)
# password = "".join(password_list)

# print(password)

# x = int(input("X: "))
# y= int(input("Y: "))

# if x< y:
#     if x== y:
#         y=2 * (x - y)
#     else:
#         y = 2 * y-5
# else:
#     y= 6 +2 * y

# print(y)





# a = int(input("A: "))
# b = int(input("B: "))

# if a <= b:
#     x = 4 * a + 7
# else:
#     x = 3 * b + a

# print(x)


# y=7
# x= 13
# x= 3* y
# y= x-y
# if x==y+7 and x%4==0:
#     if (x-x%y)%7==0:
#         print("A")
#     else:
#         print("B")
# elif x == y+7:
#     if y%7==0:
#         print("C")
#     else:
#         print("D")
# else:
#     print("E")

# rock_paper_scissors = ["""
#                         1.Rock
#                         2.Paper
#                         3.Scissors
#                        """]

# import random

# while True:
#     user_choice = int(input("Enter your choice: "))
#     computer_choice = random.randint(1,3)
#     if user_choice == computer_choice:
#         print("Draw")
#     elif user_choice == 1 and computer_choice == 2:
#         print("Computer wins")
#     elif user_choice == 2 and computer_choice == 3:
#         print("Computer wins")
#     elif user_choice == 3 and computer_choice == 1:
#         print("Computer wins")
#     else:
#         print("User wins")  
        
#     play_again = input("Do you want to play again? (yes/no): ")
#     if play_again.lower() != "yes":
#         break

# dictionary 


#  key ,value


# adlar= {
#     "ad": "Ali",
#     "soyad": "veli",
#     "yas": 20
# }

# print (adlar["ad"])

# print (adlar.values())
# print (adlar.keys())
# print (adlar.items())

# adlar['seher'] = "Baki"

# print (adlar)

# tuple

# soyadlar = ("Nuran","Eminzada","Nurzada") #deyisilmeyen


# set

# adlar = {"Nuran","Eminzada","Nurzada","Eminzada"}


# print(adlar)

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         result = 0
#         for i in range(len(s)-1):
#             if roman[s[i]] < roman[s[i+1]]:
#                 result -= roman[s[i]]
#             else:
#                 result += roman[s[i]]
#         return result + roman[s[-1]]
    