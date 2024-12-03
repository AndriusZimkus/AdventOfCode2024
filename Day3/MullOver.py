import re
with open('input.txt', 'r') as file:
        text = file.read()
	
def mul(x1,x2):
        return x1*x2



def evaluateInitial(text):
        result = 0
        while True:
                try:
                        span = re.search("mul\([0-9]+,[0-9]+\)", text).span()
                        exp = text[span[0]:span[1]]
                        expResult = eval(exp)
                        result += expResult
                        text = text[:span[0]] + text[span[1]:]
                except:
                       break
        return result     

print("Total result:", evaluateInitial(text))

def evaluateConditional(text):
        isEnabled = True
        result = 0
        while True:
                #print(text)
                
                
                if isEnabled:
                        condRegex = "don't\(\)"
                else:
                        condRegex = "do\(\)"
                        
                try:
                        span = re.search("mul\([0-9]+,[0-9]+\)", text).span()
                except:
                        span = (0,0)
                try:
                        span2 = re.search(condRegex,text).span()
                except:
                        span2 = (0,0)


                if span[1] == 0 and span2[1] == 0:
                        # No statement to execute found
                        break
                elif (span[1] != 0 and (span[0]<span2[0] or span2[1]==0)) and isEnabled:
                        #evaluate mul          
                        exp = text[span[0]:span[1]]
                        expResult = eval(exp)
                        result += expResult
                        text = text[span[1]:]
                elif span2[1] != 0:
                        #Do or don't
                        isEnabled = not isEnabled
                        text = text[span2[1]:]
                else:
                        break
                #print (result)
                        
        return result  

print("Conditional result:", evaluateConditional(text))
