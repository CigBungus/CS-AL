# temp = int(input("> "))

# if temp >= -273 and temp <= 25:
#     print("solid")

# elif temp > 26 and temp < 40:
#     print("liquid")

# else:
#     print("not found")

gapcount = 0
previousCharSpace = False

sentence = "Good  to go"

for i in range(1, len(sentence)):
    if sentence[i-1] == " ":
        gapcount += 1

        previousCharSpace = True 
    
    else: 
        previousCharSpace = False

    print(i)
    print(sentence[i-1])
    print(gapcount)
    print(previousCharSpace)

print(gapcount)
