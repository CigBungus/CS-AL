n=1
x=True
a=int(input("number: "))

while x:
    
    b=a*a
    print(f"square = {b}")
    n=n+1
    a = b+1
    if n > 5:
        x=False
