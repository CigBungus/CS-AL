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

print(daily_temp)
print(average)
print(total_average)


for i in range(1, days):
    if average[i-1] == total_average:
        print(f"on day #{i+1} the temperature was the same as the average temperature")

    elif average[i-1] > total_average:
        print(f"on day #{i+1} the temperature was higher than the average temperature")
        
    elif average[i-1] < total_average:
        print(f"on day #{i+1} the temperature was lower than the average temperature")


