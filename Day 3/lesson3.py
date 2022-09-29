# my_sentence = " aa {1} bb {1} cc {2} ".format("zz", "yy", "xx")



#print(my_sentence)


#if 10>5:
#    print("a")
#else:
#    print ("b")


# if False:
#     print("10")
# else:
#     print("20")

#print - output
#input() -  input

# my_age = input("how old are you: ")
# print(type(my_age))
#print("i am " + "my_age + " years old")







# age = 22
# age += 5 #incrementation გაზრდა


# print(age)


# a= "20"
# b= "30"
# c= "40"
# print(a+b)
# print(int(a)+int(b)+int(c))

#my_age = input("how old are you: ")

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))

# print("their sum is " + str(num1+num2))

#მომხმარებელს შემოატანინეთ ორი რიცხვი
#გამოითვალეთ მათი ნამრავლი
#თუ ნამრავლი მეტია 100-ზე, დაპრინტეთ "xxx", თუ არადა - "yyy"

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))
# product = num1 * num2
# if product > 100 :
#     print("xxx")
# else:
#     print("yyy")





# a = 7
# b = 3

# print(a + b)
# print(a * b)
# print(a / b)
# print(a - b)

# print(b % a)  #რამდენი დარჩება ნაშთი
# print(a **b) #ხარისხში აყვანა
# print(a//b)


#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
# აქედან მხოლოდ კენტები შეკრიბოს და დაპრინტოს ჯამი

# 5 % 2 = 1A
# 13 % 2 = 1
# 10 % 2 = 0
# 16 % 2 = 0


num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
num3 = int(input("enter number2: "))
sum = 0
if (num1 % 2) == 1:
    sum = sum + num1
if (num2 % 2) == 1:
    sum = sum + num2
if (num3 % 2) == 1:
    sum = sum + num3
print(sum)