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
                    initB = int(value)
                elif "Register C" in line:
                    c = int(value)
                    initC = int(value)
                elif "Program" in line:
                    program = [int(x) for x in value.split(",")]
            except:
                continue
            


    #print(program)
    print("Filename:",fileName)
    s,newA,newB,newC = executeProgram(program,a,b,c,False)

    print("Register A:",newA)
    print("Register B:",newB)
    print("Register C:",newC)
    print("Part 1 result:",s)


    a = 0
    iteration = 8**8
    a = 74538687 #7
    a = 78732909
    a = 2242993773 #9
    a = 78732909 # 8
    
    matchedCount = 0

    print("Program",program)
    while True:
        #print("A in register:",a)
            
        s,newA,newB,newC = executeProgram(program,a,b,c,True)
        matches = matchCount(s,program)

        if matches > matchedCount:

            print("Matches",matches)
            print(s)
            print("Iteration",a)
            matchedCount = matches
            iteration = matches**matches 
            #iteration*=2
            #iteration+=1
            #iteration=matches+1
            

        if s == program:
            break
        
        a+=iteration
    print("Register A:",a)
    print("Part 2 result:",s)
    print("Part 2 program:",program)
    
def matchCount(a1,a2):
    matches = 0
    for j in range (len(a1)):
        if a1[j] != a2[j]:
            return j
    return len(a1)
def executeProgram(program,a,b,c,matchProgram):
    i = 0
    s = []
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        i+=2
        #print("opcode",opcode)
        #print("operand",operand)

        s,a,b,c,i = performCommand(opcode,operand,a,b,c,s,i,matchProgram)


        if matchProgram and len(s)>len(program):
            return s,a,b,c

        if matchProgram and len(s)>0:

            for j in range (len(s)):
                if s[j] != program[j]:
                    return s,a,b,c

    return s,a,b,c
    
def performCommand(opcode,operand,a,b,c,s,i,toPrint):
    combo = getCombo(operand,a,b,c)
    if 0 and toPrint:
        print("")
        print("Performing",opcode)
        print("Operand",operand)
        print("Combo",combo)
        print("a",a)
        print("b",b)
        print("c",c)
        print("s",s)
        
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
        s.append(result)
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
    #fileNames = ["test.txt","test2.txt","test3.txt","test4.txt","test5.txt","test6.txt"]
    #fileNames = ["test7.txt"]
    fileNames = ["input.txt"]
    for fileName in fileNames:
        main(fileName)
