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

import random
import string

Password_length = int(input("Password uzunlugunu daxil edin: "))
Password_letter_count = int(input("Password herf sayini daxil edin: "))
Password_number_count = int(input("Password reqem sayini daxil edin: "))
Password_symbol_count = int(input("Password simvol sayini daxil edin: "))

password = ""

for i in range(Password_letter_count):
    password += random.choice(string.ascii_letters)

for i in range(Password_number_count):
    password += random.choice(string.digits)

for i in range(Password_symbol_count):
    password += random.choice(string.punctuation)
    

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

print(password)






