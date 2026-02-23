from colorama import *
from gridlib import Grid
from fraclib import *
from textbuttons import textbutton as tb
import os

version = "2.0"

def intInput(string=""):
    while True:
        usrInput = input(string)
        try:
            usrInput = int(usrInput)
            return usrInput
        except:
            pass
    
def fracInput(string=""):
    while True:
        usrInput = input(string)
        try:
            usrInput = frac(usrInput)
            return usrInput
        except:
            pass

def highlight(string,condition):
    if condition:
        return Fore.BLACK + Back.WHITE + string + Style.RESET_ALL
    else:
        return string
    
def generateMatrix():
    os.system("clear")
    file = open(__file__.replace("MATRIUX.py","savedMatrix.txt"))
    lines = list(file)
    file.close()
    if lines == []:
        os.system("clear")
        print("ERROR: The saved matrix has been deleted.")
        print("Press ENTER to generate a new 2x2 matrix.")
        input()
        matrixWidth = 2
        matrixHeight = 2
        array = [[tb(frac("0"),inputFrac) for i in range(matrixWidth)] for i in range(matrixHeight)]
    else:
        if lines[-1][-1] != "\n":
            lines[-1] += "\n"
        lines = [i[:-1] for i in lines]
        array = [[tb(frac(j),inputFrac) for j in i.split(" ")] for i in lines]
    return array

# BUTTON FUNCTIONS: must be formatted as 'function(usrInput,buttonRef)'
def inputFrac(usrInput,buttonRef):
    try:
        usrInput = frac(usrInput)
        buttonRef.setValue(usrInput)
    except:
        return None
    
def inputInt(usrInput,buttonRef):
    try:
        usrInput = int(usrInput)
        buttonRef.setValue(usrInput)
    except:
        return None
    
def enterReplace(usrInput,buttonRef):
    global mode
    global selectedPos

    if usrInput == "":
        selectedPos = (0,0)
        mode = ["Replace",g_replace]

def applyReplace(usrInput,buttonRef):
    if usrInput != "":
        return None
    
    global mode
    global selectedPos

    print("R" + str(selectedPos[0]))
    replaceeNum = g_replace.getElem((0,0)).value
    multiplier = g_replace.getElem((0,1)).value
    replacerNum = g_replace.getElem((0,2)).value
    for i in range(1,g_matrix.width+1):
        g_matrix.getElem((replaceeNum,i)).setValue(g_matrix.getElem((replaceeNum,i)).value + multiplier * g_matrix.getElem((replacerNum,i)).value)
    
    selectedPos = (0,0)
    mode = ["Operation select",g_menu]

def enterSwap(usrInput,buttonRef):
    global mode
    global selectedPos

    if usrInput == "":
        selectedPos = (0,0)
        mode = ["Swap",g_swap]

def applySwap(usrInput,buttonRef):
    if usrInput != "":
        return None
    
    global mode
    global selectedPos

    firstRowNum = g_swap.getElem((0,0)).value
    secondRowNum = g_swap.getElem((0,1)).value
    currentFirst = []
    currentSecond = []
    for i in range(1,g_matrix.width+1):
        currentFirst = g_matrix.getElem((firstRowNum,i))
        currentSecond = g_matrix.getElem((secondRowNum,i))
        g_matrix.setElem((firstRowNum,i),currentSecond)
        g_matrix.setElem((secondRowNum,i),currentFirst)

    selectedPos = (0,0)
    mode = ["Operation select",g_menu]

def enterScale(usrInput,buttonRef):
    global mode
    global selectedPos

    if usrInput == "":
        selectedPos = (0,0)
        mode = ["Scale",g_scale]

def applyScale(usrInput,buttonRef):
    if usrInput != "":
        return None
    
    global mode
    global selectedPos
    
    rowNum = g_scale.getElem((0,1)).value
    multiplier = g_scale.getElem((0,0)).value
    for i in range(1,g_matrix.width+1):
        g_matrix.getElem((rowNum,i)).setValue(g_matrix.getElem((rowNum,i)).value * multiplier)

    selectedPos = (0,0)
    mode = ["Operation select",g_menu]

def enterResize(usrInput,buttonRef):
    global mode
    global selectedPos

    if usrInput == "":
        selectedPos = (0,0)
        mode = ["Resize",g_resize]

def applyResize(usrInput,buttonRef):
    if usrInput != "":
        return None
    
    global mode
    global selectedPos
    global matrixWidth
    global matrixHeight
    global g_matrix
    
    matrixHeight = g_resize.getElem((0,0)).value
    matrixWidth = g_resize.getElem((0,1)).value

    array = [["this will be overwritten" for i in range(matrixWidth)] for i in range(matrixHeight)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            currentNum = g_matrix.getElem(g_matrix.getPos((i,j)))
            if currentNum == None:
                array[i][j] = tb(frac("0"),inputFrac)
            else:
                array[i][j] = currentNum

    g_matrix = Grid(array,order="yx",xDir="right",yDir="down",origin=(-1,-1))

    selectedPos = (0,0)
    mode = ["Operation select",g_menu]

def enterSave(usrInput,buttonRef):
    global mode
    global selectedPos

    if usrInput == "":
        selectedPos = (0,0)
        mode = ["Save",g_save]

def applySave(usrInput,buttonRef):
    if usrInput != "":
        return None
    
    global mode
    global selectedPos

    file = open(__file__.replace("MATRIUX.py","savedMatrix.txt"),"w")
    savedMatrix = ""
    for i in g_matrix.array:
        for j in i:
            savedMatrix += str(j) + " "
        savedMatrix = savedMatrix[:-1]
        savedMatrix += "\n"
    file.write(savedMatrix[:-1])
    file.close()

    selectedPos = (0,0)
    mode = ["Operation select",g_menu]

def enterLoad(usrInput,buttonRef):
    global mode
    global selectedPos

    if usrInput == "":
        selectedPos = (0,0)
        mode = ["Load",g_load]

def applyLoad(usrInput,buttonRef):
    if usrInput != "":
        return None
    
    global mode
    global selectedPos
    global g_matrix

    array = generateMatrix()
    
    g_matrix = Grid(array,order="yx",xDir="right",yDir="down",origin=(-1,-1))

    selectedPos = (0,0)
    mode = ["Operation select",g_menu]

def enterClear(usrInput,buttonRef):
    global mode
    global selectedPos

    if usrInput == "":
        selectedPos = (0,0)
        mode = ["Clear",g_clear]

def applyClear(usrInput,buttonRef):
    if usrInput != "":
        return None
    
    global mode
    global selectedPos
    global g_matrix

    array = [[tb(frac("0"),inputFrac) for i in range(matrixWidth)] for i in range(matrixHeight)]
    g_matrix = Grid(array,order="yx",xDir="right",yDir="down",origin=(-1,-1))

    selectedPos = (0,0)
    mode = ["Operation select",g_menu]

def exitProgram(usrInput,buttonRef):
    os.system("clear")
    print("You have exited the matrix.")
    exit()

array = generateMatrix()

g_matrix = Grid(array,order="yx",xDir="right",yDir="down",origin=(-1,-1))
g_menu = Grid([[tb("Replace",enterReplace),tb("Swap",enterSwap),tb("Scale",enterScale),tb("Resize",enterResize),tb("Save",enterSave),tb("Load",enterLoad),tb("Clear",enterClear),tb("Exit",exitProgram)]],order="yx",xDir="right",yDir="down",origin=(0,0))
g_save = Grid([[tb("SAVE",applySave)]],order="yx",xDir="right",yDir="down",origin=(0,0))
g_load = Grid([[tb("LOAD",applyLoad)]],order="yx",xDir="right",yDir="down",origin=(0,0))
g_clear = Grid([[tb("CLEAR",applyClear)]],order="yx",xDir="right",yDir="down",origin=(0,0))

matrixWidth = g_matrix.width
matrixHeight = g_matrix.height

selectedPos = (1,1)
running = True
mode = ["Element entry",g_matrix]

while running:
    if mode[0] == "Operation select":
        g_swap = Grid([[tb(1,inputInt),tb(1,inputInt),tb("APPLY!",applySwap)]],order="yx",xDir="right",yDir="down",origin=(0,0))
        g_replace = Grid([[tb(1,inputInt),tb(frac("1"),inputFrac),tb(1,inputInt),tb("APPLY!",applyReplace)]],order="yx",xDir="right",yDir="down",origin=(0,0))
        g_scale = Grid([[tb(frac("1"),inputFrac),tb(1,inputInt),tb("APPLY!",applyScale)]],order="yx",xDir="right",yDir="down",origin=(0,0))
        g_resize = Grid([[tb(matrixHeight,inputInt),tb(matrixWidth,inputInt),tb("APPLY!",applyResize)]])

    displayArray = g_matrix.getDisplayArray("right")
    matrixDisplay = ""
    for i in range(g_matrix.height):
        matrixDisplay += "R" + str(i+1) + " | "
        for j in range(g_matrix.width):
            matrixDisplay += highlight(displayArray[i][j],(g_matrix.getPos((i,j))==selectedPos) and (mode[0] == "Element entry")) + "  "
        matrixDisplay += "\n"
    matrixDisplay = matrixDisplay[:-1]

    modeDisplay = ""
    
    if mode[0] == "Element entry":
        modeDisplay = "Row " + str(selectedPos[0]) + ", element " + str(selectedPos[1])

    elif mode[0] == "Operation select":
        for i in range(g_menu.width):
            modeDisplay += highlight(str(g_menu.getElem((0,i))),selectedPos == (0,i)) + "  "
    
    elif mode[0] == "Swap":
        modeDisplay = "Swap R" + highlight(str(g_swap.getElem((0,0))),selectedPos==(0,0))
        modeDisplay += " <-> "
        modeDisplay += "R" + highlight(str(g_swap.getElem((0,1))),selectedPos==(0,1))
        modeDisplay += " ........ " + highlight(str(g_swap.getElem((0,2))),selectedPos==(0,2))

    elif mode[0] == "Replace":
        enablePlus = int(str(g_replace.getElem((0,1)))[0] != "-")
        modeDisplay = "Replace R" + str(g_replace.getElem((0,0))) + " -> "
        modeDisplay += "R" + highlight(str(g_replace.getElem((0,0))),selectedPos==(0,0))
        modeDisplay += "+"*enablePlus + highlight(str(g_replace.getElem((0,1))),selectedPos==(0,1))
        modeDisplay += "*R" + highlight(str(g_replace.getElem((0,2))),selectedPos==(0,2))
        modeDisplay += " ........ " + highlight(str(g_replace.getElem((0,3))),selectedPos==(0,3))

    elif mode[0] == "Scale":
        modeDisplay = "Scale R" + str(g_scale.getElem((0,1))) + " -> "
        modeDisplay += highlight(str(g_scale.getElem((0,0))),selectedPos==(0,0))
        modeDisplay += "*R" + highlight(str(g_scale.getElem((0,1))),selectedPos==(0,1))
        modeDisplay += " ........ " + highlight(str(g_scale.getElem((0,2))),selectedPos==(0,2))

    elif mode[0] == "Resize":
        modeDisplay = "Set dimensions to: " + highlight(str(g_resize.getElem((0,0))),selectedPos==(0,0))
        modeDisplay += "x" + highlight(str(g_resize.getElem((0,1))),selectedPos==(0,1))
        modeDisplay += " ........ " + highlight(str(g_resize.getElem((0,2))),selectedPos==(0,2))

    elif mode[0] == "Save":
        modeDisplay = "Press ENTER to confirm save: " + highlight(str(g_save.getElem((0,0))),selectedPos==(0,0))

    elif mode[0] == "Load":
        modeDisplay = "Press ENTER to confirm load: " + highlight(str(g_load.getElem((0,0))),selectedPos==(0,0))

    elif mode[0] == "Clear":
        modeDisplay = "Press ENTER to confirm deletion: " + highlight(str(g_clear.getElem((0,0))),selectedPos==(0,0))
    
    os.system("clear")
    print("MATRIUX ver " + version + " | Mode: " + mode[0])
    print("-----------------------------------------------------")
    print(modeDisplay)
    print("")
    print(matrixDisplay)
    print("")
    action = input("Action: ")

    # MOVEMENT
    if action == "w":
        selectedPos = (selectedPos[0]-1,selectedPos[1])
    elif action == "s":
        selectedPos = (selectedPos[0]+1,selectedPos[1])
    elif action == "d":
        selectedPos = (selectedPos[0],selectedPos[1]+1)
    elif action == "a":
        selectedPos = (selectedPos[0],selectedPos[1]-1)
    else:
        mode[1].getElem(selectedPos).click(action)

    if mode[1].getElem(selectedPos) == None:
        if mode[0] in ["Element entry","Swap","Replace","Scale","Resize","Save","Load","Clear"]: # Return to operation select menu
            mode = ["Operation select",g_menu]
            selectedPos = (0,0)
        elif mode[0] == "Operation select":
            mode = ["Element entry",g_matrix]
            selectedPos = (1,1)