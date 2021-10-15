numBags = int(input("num bags > "))
numSweets = int(input("num sweets > "))

if not(numBags % 2 == 0 and numSweets % 2 != 0 or numBags % 2 != 0 and numSweets % 2 == 0) and numSweets > numBags:
    listbags = []
    for i in range(numBags - 1):
        listbags.append(1)

    listbags.append(numSweets - len(listbags))

    print(listbags)

############################################################################################################################################

# while True:

#     if numSweets < numBags:
#         break
#     elif numBags % 2 == 0 and numSweets % 2 != 0 or numBags % 2 != 0 and numSweets % 2 == 0:
#         print("impossible to do")
#         break

#     else:
#         sweetInBag = numSweets // numBags

#         remainderSweets = numSweets % numBags

#         bagList = [ sweetInBag for i in range(numBags)]
#         print(bagList)
#         print(len(bagList))
#         print(remainderSweets)
#         break

    



        

        








