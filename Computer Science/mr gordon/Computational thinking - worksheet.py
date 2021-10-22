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
    if numBags % 2 == 0 and numSweets % 2 != 0:
        print("not possible.")
    elif numBags % 2 != 0 and numSweets % 2 == 0:
        print("not possible.")
    else:
        print("possible")


if __name__ == "__main__":
    inputs()





        

        








