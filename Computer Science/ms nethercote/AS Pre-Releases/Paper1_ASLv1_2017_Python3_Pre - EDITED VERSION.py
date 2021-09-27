from random import *

SOIL = '.'
SEED = 'S'
PLANT = 'P'
ROCKS = 'X'

FIELDLENGTH = 20 
FIELDWIDTH = 35 

def GetHowLongToRun(): # asks the user how many years the simulation should go for
  print('Welcome to the Plant Growing Simulation')
  print()
  print('You can step through the simulation a year at a time')
  print('or run the simulation for 0 to 5 years')
  print('How many years do you want the simulation to run?')
  YURR = True
  while YURR == True:
    try:
      Years = int(input('Enter a number between 0 and 5, or -1 for stepping mode: '))
      if Years < -1 or Years > 5:
        print("type a number between -1 and 5")
      else:
        break
    except:
      print("type a number")
  return Years # the years that the simulation will go for

def CreateNewField(): 
  Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
  Row = FIELDLENGTH // 2
  Column = FIELDWIDTH // 2
  Field[Row][Column] = SEED
  return Field

def ReadFile(): # if the user has a pre-made field this function 
  FileName = input('Enter file name: ')
  Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
  try:
    FileHandle = open(FileName, 'r')
    for Row in range(FIELDLENGTH):
      FieldRow = FileHandle.readline()
      for Column in range(FIELDWIDTH):
        Field[Row][Column] = FieldRow[Column]
    FileHandle.close()
  except:
    Field = CreateNewField() # if the user file creates an error, the program will generate a field
  return Field

def InitialiseField(): # it will generate a new field or will take a user made field 
  Response = input('Do you want to load a file with seed positions? (Y/N): ')
  if Response == 'Y':
    Field = ReadFile()
  else:
    Field = CreateNewField()
  return Field 

def Display(Field, Season, Year):
  print('Season: ', Season, '  Year number: ', Year)
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      print(Field[Row][Column], end='')
    print('|{0:>3}'.format(Row))
  print()

def CountPlants(Field):
  NumberOfPlants = 0
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == PLANT:
        NumberOfPlants += 1
  if NumberOfPlants == 1:
    print('There is 1 plant growing')
  else:  
    print('There are', NumberOfPlants, 'plants growing')
    
def SimulateSpring(Field): # will simulate spring
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == SEED:
        if randint(0,4)<2:
          Field[Row][Column] = PLANT
  CountPlants(Field)
  if randint(0, 1) == 1:
    Frost = True
  else:
    Frost = False
  if Frost:    
    PlantCount = 0
    for Row in range(FIELDLENGTH):
      for Column in range(FIELDWIDTH):
        if Field[Row][Column] == PLANT:
          PlantCount += 1
          if PlantCount % 3 == 0:
            Field[Row][Column] = SOIL
    print('There has been a frost')
    CountPlants(Field)
  return Field
 
def SimulateSummer(Field): # will simulate summer
  RainFall = randint(0, 2)
  if RainFall == 0:
    PlantCount = 0
    for Row in range(FIELDLENGTH):
      for Column in range(FIELDWIDTH):
        if Field[Row][Column] == PLANT:
          PlantCount += 1
          if PlantCount % 2 == 0:
            Field[Row][Column] = SOIL
    print('There has been a severe drought')
  CountPlants(Field)
  return Field

def SeedLands(Field, Row, Column): 
  if Row >= 0 and Row < FIELDLENGTH and Column >= 0 and Column < FIELDWIDTH: 
    if Field[Row][Column] == SOIL:
      Field[Row][Column] = SEED
  return Field

def SimulateDisease(Field, Row, Column):
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == PLANT and random.choice(1,25) == 1:
        Field[Row][Column] = SOIL
        if Field[Row + 1][Column + 1] == PLANT:
          Field[Row + 1][Column + 1] = SOIL
          if Field[Row + 2][Column + 2] == PLANT:
            Field[Row + 2][Column + 2] == SOIL

  return Field
  SimulateAutumn(Field)
        
  
def SimulateAutumn(Field): # will simulate autumn
  
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == PLANT:
        Field = SeedLands(Field, Row - 1, Column - 1)
        Field = SeedLands(Field, Row - 1, Column)
        Field = SeedLands(Field, Row - 1, Column + 1)
        Field = SeedLands(Field, Row, Column - 1)
        Field = SeedLands(Field, Row, Column + 1)
        Field = SeedLands(Field, Row + 1, Column - 1)
        Field = SeedLands(Field, Row + 1, Column)
        Field = SeedLands(Field, Row + 1, Column + 1)
  return Field

def SimulateWinter(Field): # will simulate winter
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == PLANT:
        Field[Row][Column] = SOIL
  return Field

def SimulateOneYear(Field, Year): # will simulate all the seasons in one year
  Field = SimulateSpring(Field)
  Display(Field, 'spring', Year)
  Field = SimulateSummer(Field)
  Display(Field, 'summer', Year)
  Field = SimulateDisease(Field, Row, Column)
  Display(Field, 'autumn', Year)
  Field = SimulateWinter(Field)
  Display(Field, 'winter', Year)

def Simulation():
  YearsToRun = GetHowLongToRun() # amount of years that it will run for
  if YearsToRun != 0:
    Field = InitialiseField()
    if YearsToRun >= 1:
      for Year in range(1, YearsToRun + 1):
        SimulateOneYear(Field, Year)
    else:
      Continuing = True                     
      Year = 0
      while Continuing: # will run the program untill the user types "x"
        Year += 1
        SimulateOneYear(Field, Year)
        Response = input('Press Enter to run simulation for another Year, Input X to stop: ')
        if Response == 'x' or Response == 'X':
          Continuing = False
    print('End of Simulation')

   
if __name__ == "__main__":
  Simulation()      
   
   
