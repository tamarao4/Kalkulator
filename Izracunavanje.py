""" izracunavanje izraza koji su napisani postfiksno """
import math

from Stek import Stack


OPERANDI = "0123456789"

def operacije(operator, a, b):
    if operator == "^":
        return math.pow(b, a)
    elif operator == "*":
        return  a*b 
    elif operator == "/":
        return b/a
    elif operator == "+":
        return a+b 
    else: 
        return b-a
    
def izracunaj(postfixno):   
    
    operandi = Stack()
    znakovi = postfixno.split()
    
    for znak in znakovi:
        if znak[0] in OPERANDI:
            operandi.push(float(znak))
        else:
            prvi = operandi.pop()          
            drugi = operandi.pop()
            
            rezultat = operacije(znak, prvi, drugi)
            operandi.push(rezultat)
    
    if len(operandi) > 1:
        raise Exception('invalid syntax')
    
    return operandi.pop()
            
            
if __name__ == "__main__":
    print ("Resenje")
    print (izracunaj (" 2 3 ^"))
    #print izracunaj ("4 8 6 5 - * 3 2 - 2 2 + * /")