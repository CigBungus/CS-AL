import random

# 118

# def number():
#     num = int(input("enter a number: "))
#     count(num)
#     return num

# def count(num):
#     for i in range(1, num+1):
#         print(i)

# number()

########################################

# 119

# def numbers():
#     low = int(input("enter a low number: "))
#     high = int(input("enter a high number: "))

#     comp_num = random.randint(low, high)
#     print(comp_num)
#     guess(comp_num)
#     return comp_num

# def guess(comp_num):
#     player_guess = int(input("guess the number that i am thinking of: "))
#     check(player_guess, comp_num)
#     return player_guess

# def check(player_guess, comp_num):
#     if player_guess == comp_num:
#         print("correct you win")

#     else:
#         guess(comp_num)


# numbers()

########################################

# 120

# def menu():
#     print("1) Addition\n2) Subtraction")
#     menu_choice = int(input("Enter 1 or 2: "))
    
#     if menu_choice == 1:
#         addition()

#     elif menu_choice == 2:
#         subtraction()

# def addition():
#     num1 = random.randint(5, 20)
#     num2 = random.randint(5, 20)
#     answer = num1 + num2
#     user_answer = int(input(f"what is {num1}+{num2}? "))
#     check(answer, user_answer)
#     return answer, user_answer

# def subtraction():
#     num1 = random.randint(25, 50)
#     num2 = random.randint(1, 25)
#     answer = num1 - num2
#     user_answer = int(input(f"what is {num1}-{num2}? "))
#     check(answer, user_answer)
#     return answer, user_answer

# def check(answer, user_answer):
#     if answer == user_answer:
#         print("correct")
#     else:
#         print(f"incorrect\nthe correct answer is {answer}")

# menu()
    
    

