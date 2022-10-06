# name1 = input("enter name1: ")
# name2 = input("enter name2: ")

# amount_of_vowels_in_name1 = 0
# amount_of_vowels_in_name2 = 0

# for char in name1:
#     if char in "aeiou":
#         amount_of_vowels_in_name1 += 1

# for char in name2:
#     if char in "aeiou":
#         amount_of_vowels_in_name2 += 1

# if amount_of_vowels_in_name1 > amount_of_vowels_in_name2:
#     print("the amount of vowels in nam1 is more and it contains {} vowels".format(amount_of_vowels_in_name1))
# elif amount_of_vowels_in_name1 < amount_of_vowels_in_name2:
#     print("the amount of vowels in nam2 is more and it contains {} vowels".format(amount_of_vowels_in_name2))
# else:
#     print ("they have equal amount of vowells")




# my_name = "nika"

#itteration - იტერაცია --- გამეორება

#ამ შემთხცვევაში char არის საიტერაციო ცვლადი

# for char in my_name:
#     print(char)

# არის საიტერაციო ცვლადი ამ შემთხვევაში
# for i in range(10):
#     print(i)


#მომხმარებელლს შემოატანინე ორი სახელი და ის დამიპრინტე
# რომლის სახელსაც მეტი თანხმოვანი იქნება

# print(5 != 10)

# print("a" not in "kjkszpj")

name1 = input("enter name1: ")
name2 = input("enter name2: ")

amount_of_consonant_in_name1 = 0
amount_of_consonant_in_name2 = 0

for char in name1:
    if char not in "aeiou":
        amount_of_consonant_in_name1 += 1

for char in name2:
    if char not in "aeiou":
        amount_of_consonant_in_name2 += 1

if amount_of_consonant_in_name1 > amount_of_consonant_in_name2:
    print(format(name1))
elif amount_of_consonant_in_name1 < amount_of_consonant_in_name2:
    print(format(name2))
else:
    print ("they have equal amount of consonants")
