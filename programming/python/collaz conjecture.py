import time
import sys
import os

x = int(input("enter any number: "))




time.sleep(0.1)
os.system("cls")

print(len(str(x))*"@" + f"       {x}")

while x != 1:

    if x % 2 == 0:
        x = x / 2
        print(f"down {x}")
        time.sleep(0.1)
        # os.system("cls")

    else:
        x = (x * 3) + 1
        print(f"up {x}")
        time.sleep(0.1)
        # os.system("cls")

    # print((len(str(x))-2)*"@" + f"       {x}")

