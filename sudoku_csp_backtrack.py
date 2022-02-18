# -*- coding: utf-8 -*-

cols = "123456789"
rows = "ABCDEFGHI"

def InputData(inputPath):
  #initialization

    grid = []
    s1=''
    s2= ''
    s3= ''
    iter = 0
    count = 0
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    tempList = []
    c = 0 #counter
  #Read Input File and convert it to suitable format
    with open(inputPath, "r") as inputFile:
        for line in inputFile:
            for i in line:
                if i == '|':
                    c+=1
                    if c >= 2:
                        s1 += '0'
                if i in numbers:
                    s1 += i
                    c=0
    for iter,i in enumerate(s1[:-9]):
      if iter != 0 and iter%10 == 0:
        s3 += ''
      else:
        s3 += i
    s3 = s3[:-1]
    s3 += s1[-9:]
    inputFile.close()
    return s3

inputPath = '/content/Demo Input - Copy.txt' #path where input matrix is stored

InputStr = InputData(inputPath)

def plot(rows, cols):
  joinGrid = []

  for x in range(len(rows)):
    for y in range(len(cols)):
      joinGrid.append(rows[x] + cols[y])
  return joinGrid


sudokuGrid = plot(rows, cols) #List of all 81 possible grid locations


class AC3:
  def __init__(self, domain = cols, grid = ""):
    self.grid = sudokuGrid
    self.domain = self.Matrix(grid)  #get the domain of the CSP
    self.values = self.Matrix(grid)  #the values of the CSP
    self.lists = self.addTogether()  #making a sudoku square
    self.aList = self.get_grid()     #assigning each sudoku square
    self.bList = self.get_a()        #get the difference
    self.constriant = self.get_constriants()  #get the Constraints 
  def get_rows(self): #getting the rows of the sudoku
    a = []
    for x in range(len(rows)):
      a.append(plot(rows[x], cols))
    return a

  def get_cols(self): #getting the columns of the sudoku
    b = []
    for y in range(len(cols)):
      b.append(plot(rows, cols[y]))

    return b

  def get_box(self): #getting a 3x3 box of the sudoku
    z = []

    for c in ('ABC','DEF','GHI'):
      for d in ('123','456','789'):
        z.append(plot(c, d))
    return z

  def addTogether(self): #each square of the 3x3 box in teh sudoku
    a = []
    b = []
    c = []
    d = []
    a = self.get_rows()
    b = self.get_cols()
    c = self.get_box()

    d = b + a + c

    return d

  def get_grid(self): #assigning each square in the 9x9 sudoku
    return dict((x, [u for u in self.lists if x in u]) for x in sudokuGrid)

  def get_a(self): #finding the neighbouring elements given a sudoku square 
    a = dict((x, set(sum(self.aList[x],[]))-set([x])) for x in sudokuGrid)
    return a

  def get_constriants(self): #finding the constriants 
    constraints = {(x, y) for x in self.grid for y in self.bList[x]}
    return constraints

  def Matrix(self, grid=""): #fills in a grid
    values = dict()
    for x in range(len(self.grid)):
      if grid[x]!='0':
        values[self.grid[x]] = grid[x]
      else:
        values[self.grid[x]] = cols
    return values
  def rev(self,x1,x2): #checks to see if something is breaking a rule
    r = False
    values = self.values[x1]
    for i in values:
      for j in self.values[x2]:
        if not(j!=i and x2 in self.bList[x1]):
          self.values[x1] = self.values[x1].replace(x1, '')
          r = True
      return r

  def AC3(self): #checks the constraints and checks if everything is good
    q = []

    for i in self.constriant:
      q.insert(0,i)
    i = 0

    while q:
      (x1,x2) = q.pop() 
      i = i + 1
      rv = AC3.rev(self,x1,x2)
      if (rv == True):
        for x3 in (self.bList[x1]):
          q.append((x3, x1))
        if len(self.values[x1]) == 0:
          return False          
      return True

  def isComplete(self):  #checks to see if AC3 is complete
    for variable in sudokuGrid:
      if len(self.values[variable])>1:
        return False
      return True
AC3(grid=InputStr)

## backtracking starts from here
if (AC3(grid=InputStr).isComplete()): 
    emptyGrid = [0, 0]
    def safe(sudoku):  #checks to see if a location is empty and assigns it to the grid and returns true if it is
        for x in range(9):
            for y in range(9):
                if(sudoku[x][y] == 0):
                    emptyGrid[0],emptyGrid[1] = x, y
                    return True
        return False

    def used(sudoku, row, col, target): #checks rows and cols and boxes
        val = False
        for y in range(9):
            if(sudoku[row][y] == target):
                val = True
        for x in range(9):
            if(sudoku[x][col] == target):
                val = True
        row =  row - row % 3
        col =  col - col % 3
        for i in range(3):
            for j in range(3):
                if(sudoku[i + row][j + col] == target):
                    val =  True
        return val

    def solve_sudoku(sudoku): #recurrsively calls itself to intiate backtracking

        if(safe(sudoku) == False): #check if safe
            return True
        row = emptyGrid[0]
        col = emptyGrid[1]

        for target in range(1, 10): #iterates through the values 1 to 10
            if(not used(sudoku,row,col,target)):
                sudoku[row][col] = target # assigns a value if the variable is in the domain of the location

                if(solve_sudoku(sudoku) == True): #calls itself reccursively
                    return True

                sudoku[row][col] = 0 #resets itself and tries again
                  
        return False

    def parsegrid(): #parsing the given input
        temp = []
        grid=[]
        for iter,i in enumerate(lineList):
          temp.append(int(i))
          if len(temp)%9 == 0 and iter!=0:
            grid.append(temp)
            temp = []
        return grid

    def OutputToFile(grid): #outputs to a text file
      f = open("output.txt", "w")
      for i in grid:
        for j in i:
          print(f'|{j}',end="",file = f)
        print('|',file=f)
      f.close()
      pass

    grid = parsegrid()
    if(solve_sudoku(grid)):
        OutputToFile(grid)
    else:
        print ("No solution exists")

# f = open("output.txt", "r") #Code for checking
# for i in f:
#   print(i)
# f.close()
