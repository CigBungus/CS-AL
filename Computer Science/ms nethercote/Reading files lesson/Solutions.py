### task 1 solution ###

file = open("Task1.txt", "r") # opens a file to read it
file_lines = file.readlines() # reads each seperate line of the file
file.close() # closes the file

for i in file_lines:
    print(i.strip(" ,\n")) # prints eeach line and removes and commas or spaces


### task 2 solution ###
    
file = open("Task2.txt", "r")
data = file.read()

countA = 0
countS = 0
countD = 0
countF = 0

for letter in data:
    if letter == 'A' or letter =='a':
        countA += 1
    elif letter == 'S' or letter =='s':
        countS += 1
    elif letter == 'D' or letter =='d':
        countD += 1
    elif letter == 'F' or letter =='f':
        countF += 1
        
file.close()

print('A or a:',countA)
print('S or s:',countS)
print('D or d:',countD)
print('F or f:',countF)


### task 3 solution ###
    
