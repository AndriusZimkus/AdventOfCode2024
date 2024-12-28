def main():
 
    fileName = "test6.txt"
    path = "../../Advent Of Code Cases/Day21/" + fileName

    codes = []
    with open(path, 'r') as file:
        for line in file:
            codes.append(line.strip())

    print(codes)
    
    getNumpad()
    getKeypad()
    getNumpadMatrix()

    complexities = getCodeComplexities_2_BFS(codes)

    print("Complexities:",complexities)

def getCodeComplexities_2_BFS(codes):
    cnp = (2,3)
    ckp = (2,0)
    complexities = 0

    for code in codes:
        print(code)

        #Get all shortest numpad paths
        paths = getPaths(code,cnp)
        print(paths)

    return complexities

def getPaths(code,cp):
    paths = []
    shortestPathLength = 0
    letterPos = 1
    
    neededLetter = code[:letterPos]
    print(neededLetter)
    x = cp[0]
    y = cp[1]
    
    return paths

def getPaths_DFS(code,cp):
    shortestPathLength = 0
    letterPos = 1
    neededLetter = code[:letterPos]
    
    print(neededLetter)

    x = cp[0]
    y = cp[1]

    def explorePath(neededLetter,cp,path,step):
        global numpad
        nonlocal shortestPathLength
        print("CP",cp)
        x = cp[0]
        y = cp[1]
        if x < 0 or y < 0:
            return []
        if x == 0 and y == 3:
            return []
        try:
            cell = numpad[y][x]
        except:
            return []

        print("Cell")


        if cell == neededLetter:
            if len(path) == shortestPathLength or shortestPathLength == 0:
                shortestPathLength = len(path)
                return [path]
            else:
                return []    
        
        return (explorePath(neededLetter,(x+1,y),path+">",">")
         + explorePath(neededLetter,(x-1,y),path + "<","<")
         + explorePath(neededLetter,(x,y+1),path+"v","v")
         + explorePath(neededLetter,(x,y-1),path + "^","^")
         )

    paths = (explorePath(neededLetter,(x+1,y),">",">")
         + explorePath(neededLetter,(x-1,y),"<","<")
         + explorePath(neededLetter,(x,y+1),"v","v")
         + explorePath(neededLetter,(x,y-1),"^","^")
         )

    return paths

    
def getCodeComplexities_1_naive(codes):
    cnp = (2,3)
    ckp = (2,0)
    complexities = 0
    for code in codes:
        
        numpadStrokes = ""
        symbolStrokes = []
        for symbol in code:

            cnp,currentStrokes = getNumpadStrokes(cnp,symbol)
            symbolStrokes.append(currentStrokes)
            numpadStrokes += currentStrokes


        firstKeypadStrokes = ""
        fp = []

        firstKeypadSymbolStrokes = {}
        for ss in symbolStrokes:

            for symbol in ss:
                ckp,currentStrokes = getKeypadStrokes(ckp,symbol,False)
                
                fp.append(currentStrokes)
                firstKeypadStrokes += currentStrokes


        secondKeypadStrokes = ""

        for f in fp:

            for symbol in f:
                ckp,currentStrokes = getKeypadStrokes(ckp,symbol,False)
                secondKeypadStrokes += currentStrokes

        codeAsNumber = getCodeNumeric(code)

        codeComplexity = len(secondKeypadStrokes) * codeAsNumber
        complexities += codeComplexity
        
    return complexities

def getCodeNumeric(code):
    code = code[:3]
    return int(code)

def getKeypadStrokes(ckp,symbolToInput,toPrint):
    neededCoords = keypad[symbolToInput]

    strokes = ""

    currentStrokes = getKeypadStrokesFromTo(ckp,neededCoords)
    currentStrokes+="A"
    #v<<A>>^A<A>AvA<^AA>A<vAAA>^A
    if toPrint:
        print("CKP",ckp)
        print("NC",neededCoords)
        print("STI",symbolToInput)
        print("CS", currentStrokes)
    strokes += currentStrokes
    
    ckp = neededCoords

    return ckp,strokes

def getKeypadStrokesFromTo(c1,c2):
    x1 = c1[0]
    x2 = c2[0]
    y1 = c1[1]
    y2 = c2[1]
    strokes = ""
    if y2>y1:
        strokes += "v"*(y2-y1)
    if x2>x1:
        strokes += ">"*(x2-x1)
    if y1>y2:
        strokes += "^"*(y1-y2)
    if x1>x2:
        strokes += "<"*(x1-x2)

    return strokes

def getNumpadStrokes(cnp,numberToInput):
    neededCoords = numpad[numberToInput]

    strokes = ""

    strokes += getNumpadStrokesFromTo(cnp,neededCoords)
    strokes+="A"
    cnp = neededCoords

    return cnp,strokes

def getNumpadStrokesFromTo(c1,c2):
    x1 = c1[0]
    x2 = c2[0]
    y1 = c1[1]
    y2 = c2[1]
    strokes = ""
    if x2>x1:
        strokes += ">"*(x2-x1)
    if y2>y1:
        strokes += "v"*(y2-y1)
    if y1>y2:
        strokes += "^"*(y1-y2)
    if x1>x2:
        strokes += "<"*(x1-x2)

    return strokes

def getNumpadMatrix():
    global numpadMatrix
    numpadMatrix = [["7","8","9"],["4","5","6"],["1","2","3"],["","0","A"]]
    
def getNumpad():
    global numpad
    numpad = {}
    numpad['7'] = (0,0)
    numpad['8'] = (1,0)
    numpad['9'] = (2,0)
    numpad['4'] = (0,1)
    numpad['5'] = (1,1)
    numpad['6'] = (2,1)
    numpad['1'] = (0,2)
    numpad['2'] = (1,2)
    numpad['3'] = (2,2)
    numpad['0'] = (1,3)
    numpad["A"] = (2,3)

def getKeypad():
    global keypad
    keypad = {}
    keypad["^"] = (1,0)
    keypad["A"] = (2,0)
    keypad["<"] = (0,1)
    keypad["v"] = (1,1)
    keypad[">"] = (2,1)
    
if __name__ == "__main__":
    main()
