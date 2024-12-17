def main(fileName):
 
       
    path = "../../Advent Of Code Cases/Day17/" + fileName
    
    with open(path, 'r') as file:
        i = 1
        for line in file:
            line = line.strip()
            try:
                value = line.split(":")[1].strip()

                if "Register A" in line:
                    a = int(value)
                elif "Register B" in line:
                    b = int(value)
                elif "Register C" in line:
                    c = int(value)
                elif "Program" in line:
                    program = [int(x) for x in value.split(",")]
            except:
                continue
            
    i = 0
    s = ""
    #print(program)
    print("Filename:",fileName)
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        i+=2
        #print("opcode",opcode)
        #print("operand",operand)

        s,a,b,c,i = performCommand(opcode,operand,a,b,c,s,i)


    print("Register A:",a)
    print("Register B:",b)
    print("Register C:",c)
    print("Result:",s)

def performCommand(opcode,operand,a,b,c,s,i):
    combo = getCombo(operand,a,b,c)
    #print(combo)
    if opcode == 0:
        result = adv(a,combo)
        return s,result,b,c,i
    elif opcode == 1:
        result = b ^ operand
        return s,a,result,c,i
    elif opcode == 2:
        result = combo % 8
        return s,a,result,c,i
    elif opcode == 3:
        if a == 0:
            return s,a,b,c,i
        else:
            return s,a,b,c,operand
    elif opcode == 4:
        result = b ^ c
        return s,a,result,c,i
    elif opcode == 5:
        result = combo % 8
        s = addToString(s,result)
        return s,a,b,c,i
    elif opcode == 6:
        result = adv(a,combo)
        return s,aresult,c,i
    elif opcode == 7:
        result = adv(a,combo)
        return s,a,b,result,i
        
def adv(a,combo):
    numerator = a
    denominator = 2**combo
    result = numerator // denominator
    return result
        
def addToString(s,result):
    if s == "":
        return str(result)
    else:
        return s + "," + str(result)
        
def getCombo(operand,a,b,c):
    if operand < 4:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        return -1

    
if __name__ == "__main__":
    fileNames = ["test.txt","test2.txt","test3.txt","test4.txt","test5.txt","test6.txt"]
    fileNames = ["input.txt"]
    for fileName in fileNames:
        main(fileName)
