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

print(f"the dailt temperatures were: {daily_temp}")
print(f"the daily averages were: {average}")
print(total_average)

same = 0
higher = 0
lower = 0

for i in range(0, days):
    if average[i-1] == total_average:
        same += 1
    elif average[i-1] > total_average:
        higher + 1
        
    elif average[i-1] < total_average:
        lower += 1

print(f"the temperature was higher than the average in {higher} of the days")
print(f"the temperature was lower than the average in {lower} of the days")
print(f"the temperature was the same as the average in {same} of the days")

