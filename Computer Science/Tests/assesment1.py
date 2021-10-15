
# asks the user to enter the first and second words
word1 = input("enter the first word: ")
word2 = input("enter the second word: ")

# a loop that iterates through each letter of word1 and checks if its in word2
# if the letters in word1 are in word2 it will return true and if not it returns false
for i in word1:
    if i in word2:
        boolean = True
      
    if not(i in word2):
        boolean = False


if boolean == True:
    print("the first word can be made from the second word")
    
elif boolean == False:
    print("the first word cannot be made from the second word ")


# asks user for number if number <= 1 breaks program
def number():
    User_number = int(input("enter a number: "))
    if User_number <= 1:
        print("not greater than 1")
    else:

        isprime(User_number)


'''

# checks if the number is prime by cycling through the numbers smaller than the number and mod divides the number by the iteration. if it returns something then its a prime if its 0 it is 
def isprime(User_number):
    prime = 1
        
    for i in range(2, User_number-1):

        if User_number % i == 0:
            prime = 0
            break
            
        elif User_number % i != 0:
            prime = 1
            
    if prime == 0:
        print("is not prime")
        
    elif prime != 0:
        print("is prime")
        
    repeat()
        
def repeat():
    choice = input("do you want to repeat? [y, n]: ")
    if choice.lower() == "y":
        number()
    
number()
        
'''

   


