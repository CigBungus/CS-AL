'''

# task 2
class Animal:
    def __init__(self, s, n):
        self.state = s
        self.size = n

    def feed(self):
        self.size += 1
        if self.size == 5:
            self.state = "FISH"

    def getState(self):
        return self.state

    def getSize(self):
        return self.size

# task 3
thisFish = Animal("Fish", 1)

print(f"{thisFish.getSize()} is the size of {thisFish.getState()}")

while thisFish.getState() != "FISH":
    thisFish.feed()
print(f"{thisFish.getState()} is now {thisFish.getSize()} in size")

print(f"it is now a big {thisFish.getState()}")

'''

# task 4
class car:
    def __init__(self, registration, make, mileage, dateOfInspection):
       self.registration = registration
       self.make = make
       self.mileage = 0
       self.dateOfInspection = dateOfInspection

    def get_registration(self):
        return self.registration

    def get_make(self):
        return self.make

    def get_mileage(self):
        return self.mileage

    def get_dateOfInspection(self):
        return self.dateOfInspection



        