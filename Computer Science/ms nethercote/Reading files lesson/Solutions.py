#######################
### task 1 solution ###
#######################

file = open("Task1.txt", "r") # opens a file
file_lines = file.readlines() # reads each seperate line of the file
file.close() # closes the file

for i in file_lines:
    print(i.strip(" ,\n")) # prints eeach line and removes and commas or spaces


#######################
### task 2 solution ###
#######################
  
file = open("Task2.txt", "r") # opens a file
data = file.read() # reads the file

countA = 0
countS = 0
countD = 0
countF = 0

# for loop that checks if the letters A, S, D, F are in the file
for letter in data:
    if letter == 'A' or letter =='a':
        countA += 1
    elif letter == 'S' or letter =='s':
        countS += 1
    elif letter == 'D' or letter =='d':
        countD += 1
    elif letter == 'F' or letter =='f':
        countF += 1
        
file.close() # closes file

# displays how many times the letter was in the file
print('A or a:',countA)
print('S or s:',countS)
print('D or d:',countD)
print('F or f:',countF)


#######################
### task 3 solution ###
#######################

file = open('Task3.txt','r')
output = file.read().split('\n')

for i in range(len(output)):
    output[i] = output[i].split(',')
    
print(output)


#######################
### task 4 solution ###
#######################

file = open("Task4.txt", "r") # opens a file
data = file.read() # reads the file
words = data.split() # splits the data into seperate words

count = 0

# for loop increases count everytime the word "the" is found
for i in words:
    if i == "the" or i == "The":
        count += 1
        
file.close() # closes file

print(f"The word 'the' is repeated {count} times in the file") # prints output


#######################
### task 5 solution ###
#######################

file = open("Task5.txt", "r") # opens file
data = file.read() # reads file
words = data.split() # splits file into words

# for loop that checks lenght of each word and prints it if word < 4 characters
for i in words:
    if len(i) < 4:
        print(i) # displays word
        
file.close() # closes file

