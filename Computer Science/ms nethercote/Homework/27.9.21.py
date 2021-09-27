# a program which makes use of case statements


NAMES = {
    "Daniele": "Golzio",
    "Dante": "Fernando",
    "Royce": "Chan",
    "Ilhan": "Shahril",
    "Ayman": "Amghar"
}

 

def main():
    print("NAMES: \nDaniele\nDante\nRoyce\nIlhan\nAyman\n")
    name = input("enter a name: ")
    lastName = NAMES.get(name.title(), "unknown name")
    print(f"{name.title()}'s last name is {lastName}")

main()



