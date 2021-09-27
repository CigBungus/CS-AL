def task1_1i():

    '''

            slow = 0
            medium = 0
            fast = 0
    INPUTDATA
            timeTaken = USERINPUT
            IF timeTaken = 0 GOTO PRINT
            IF timeTaken < 30 GOTO UNDER30
            IF timeTaken <60 GOTO UNDER60
            slow = slow + 1
            GOTO INPUTDATA
    UNDER30
            fast = fast + 1
            GOTO INPUTDATA
    UNDER60
            medium = medium + 1
            GOTO INPUTDATA
    PRINT
    OUTPUT fast, medium, slow

    '''

    slow = 0
    medium = 0
    fast = 0

    t = int(input("time: "))


    while True:
        if t > 60:
            slow += 1
            break
        if t == 0:
            break
        elif t < 30:
            fast += 1
            break
        elif t < 60:
            medium += 1
            break


    print(slow, medium, fast)




def task1_2a():
    
    num = int(input("enter a 3 digit number: "))

    print(f"The digits are {num//100} {(num%100)//10} {num%10}")



def task1_2b():
    while True:
        try:
            num = int(input("enter a 3 digit number: "))
            if len(str(num)) > 3:
                print("num too big")
            else:
                break
        except ValueError:
            print("only int")
    
    num1 = num//100
    num2 = (num%100)//10
    num3 = num%10

    print(f"{num1**3} + {num2**3} + {num3**3} =")
    print((num1**3)+(num2**3)+(num3**3))
    
    
