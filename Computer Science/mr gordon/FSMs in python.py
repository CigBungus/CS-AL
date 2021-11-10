    
while True:    
    string = input("enter a series of a's and b's: ")

    node = None
    dead_end = None
    current_node = "s0"
    end = True
    counter = 0

    for i in string:
        counter += 1

        if current_node == "s2" and counter != len(string):
            print("not possible")
            end = False
            break
        # s0
        if i == "a" and current_node == "s0":
            current_node = "s2" 
        
        elif i == "b" and current_node == "s0":
            current_node = "s1"
        # s1
        if i == "a" and current_node == "s1":
            current_node = "s0"

        elif i == "b" and current_node == "s1":
            current_node = "s1"


    if end == True and current_node == "s2":
        print("possible")
    elif end == True and current_node != "s2":
        print("not possible")

    
    

