def main():
 
    fileName = "test2.txt"
    path = "../../Advent Of Code Cases/Day21/" + fileName

    codes = []
    with open(path, 'r') as file:
        for line in file:
            codes.append(line.strip())

    print(codes)

    cnp = (2,3)
    global numpad
    numpad = {}
    numpad[7] = (0,0)
    numpad[8] = (1,0)
    numpad[9] = (2,0)
    numpad[4] = (0,1)
    numpad[5] = (1,1)
    numpad[6] = (2,1)
    numpad[1] = (0,2)
    numpad[2] = (1,2)
    numpad[3] = (2,2)
    numpad[0] = (1,3)
    numpad["A"] = (2,3)

    global keypad
    keypad = {}
    ckp = (2,0)
    keypad["^"] = (1,0)
    keypad["A"] = (2,0)
    keypad["<"] = (0,1)
    keypad["v"] = (1,1)
    keypad[">"] = (1,2)
    
    print(keypad)

    print(inputNumber(cnp,ckp,0))

def inputNumber(cnp,ckp,numberToInput):
    neededCoords = numpad[numberToInput]
    neededCoords2 = numpad["A"]

    
    
    return inputs
    
if __name__ == "__main__":
    main()
