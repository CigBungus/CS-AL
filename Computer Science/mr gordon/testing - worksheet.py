average = []
daily_temp = []
day = 0
while True:
    day += 1
    print(f"day #{day}")
    max_temp = int(input("MAX TEMPERATURE: "))
    if max_temp == 999:
        break   

    min_temp = int(input("MIN_TEMPERATURE: "))

    average_of_day = (max_temp + min_temp) / 2
    
    average.append(average_of_day)
    daily_temp.append(max_temp)
    daily_temp.append(min_temp)

days = len(average)

total_average = sum(average) / 2

for i in range(days-1):
    if average[i] == total_average:
        print(f"on day #{i+1} the temperature was the same as the average temperature")

    elif average[i] > total_average:
        print(f"on day #{i+1} the temperature was higher than the average temperature")
        
    elif average[i] < total_average:
        print(f"on day #{i+1} the temperature was lower than the average temperature")


