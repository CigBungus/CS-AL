
def task2():
    class Animal:
        def __init__(self, s, n):
            self.state = s
            self.size = n

        def feed(self):
            self.size += 1
            if self.size == 5:
                self.state = "FISH"

    animal1 = Animal(1, "fish")
    print(animal1.feed)
            
    





        