def main():
 
    fileName = "test6.txt"
    path = "../../Advent Of Code Cases/Day21/" + fileName

    codes = []
    with open(path, 'r') as file:
        for line in file:
            codes.append(line.strip())

    print(codes)

    cnp = (2,3)
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

    global keypad
    keypad = {}
    ckp = (2,0)
    keypad["^"] = (1,0)
    keypad["A"] = (2,0)
    keypad["<"] = (0,1)
    keypad["v"] = (1,1)
    keypad[">"] = (2,1)
    
    complexities = 0
    cnp = (2,3)
    ckp1 = (2,0)
    ckp2 = (2,0)
    for code in codes:
        
        numpadStrokes = ""
        symbolStrokes = []
        for symbol in code:
            #print(symbol)
            cnp,currentStrokes = getNumpadStrokes(cnp,symbol)
            symbolStrokes.append(currentStrokes)
            numpadStrokes += currentStrokes
        print(numpadStrokes)

        firstKeypadStrokes = ""
        fp = []
        #ckp = (2,0)
        firstKeypadSymbolStrokes = {}
        for ss in symbolStrokes:
            print("SS",ss)
            for symbol in ss:
                ckp1,currentStrokes = getKeypadStrokes(ckp1,symbol,False)
                
                fp.append(currentStrokes)
                firstKeypadStrokes += currentStrokes
        print (firstKeypadStrokes)

        secondKeypadStrokes = ""
        #ckp = (2,0)
        for f in fp:
            print("F",f)
            for symbol in f:
                ckp2,currentStrokes = getKeypadStrokes(ckp2,symbol,False)
                secondKeypadStrokes += currentStrokes
                print("CS",currentStrokes)
        print (secondKeypadStrokes)
        print(len(secondKeypadStrokes))
        codeAsNumber = getCodeNumeric(code)
        print(codeAsNumber)
        codeComplexity = len(secondKeypadStrokes) * codeAsNumber
        complexities += codeComplexity
        
    print("Complexities:",complexities)

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
    
if __name__ == "__main__":
    main()
