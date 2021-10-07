temp = []
average = []

while True:
    max_temp = int(input("MAX TEMPERATURE: "))
    if max_temp == 999:
        break
        
    min_temp = int(input("MIN_TEMPERATURE: "))

    
    temp.append(max_temp)
    temp.append(min_temp)

    print(temp)



