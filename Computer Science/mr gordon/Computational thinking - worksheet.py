
# tells you if the bags and sweets problem is possible

# def inputs():
#     numBags = int(input("num bags > "))
#     numSweets = int(input("num sweets > "))
#     inputcheck(numBags, numSweets)
#     return numBags, numSweets  
    

# def inputcheck(numBags, numSweets):
#     if numSweets < numBags:
#         print("the number of sweets has to be bigger than the number of bags")
#         inputs()
#     output(numBags, numSweets)

# def output(numBags, numSweets):
#     if numBags % 2 == 0 and numSweets % 2 != 0:
#         print("not possible.")
#     elif numBags % 2 != 0 and numSweets % 2 == 0:
#         print("not possible.")
#     else:
#         print("possible")


# if __name__ == "__main__":
#     inputs()


# shows how many sweets are in each bag

def inputs():
    numBags = int(input("num bags > "))
    numSweets = int(input("num sweets > "))
    inputcheck(numBags, numSweets)
    return numBags, numSweets

def inputcheck(numBags, numSweets):
    if numSweets < numBags:
        print("the number of sweets has to be bigger than the number of bags")
        inputs()
    output(numBags, numSweets)  

def output(numBags, numSweets):
    # even spread
    initial_sweets_perBag = numSweets // numBags
    remainder = numSweets % numBags

    counter = 0
    for i in range(numBags):
        counter += 1
        if counter != remainder:
            print(f"bag {i + 1} has {initial_sweets_perBag + 1} sweets")
        elif counter == remainder:
            print(f"bag {i + 1} has {initial_sweets_perBag} sweets")


    # uneven spread
    # for i in range(numBags - 1):
    #     print(f"bag {i + 1} has {1} sweet")
    # print(f"bag {numBags} has {numSweets - (numBags - 1)} sweets")

if __name__ == "__main__":
    inputs()

    









        

        








