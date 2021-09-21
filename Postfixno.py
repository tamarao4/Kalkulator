""" prebacivanje izraza iz infiksnog oblika u postfiksni """


from Stek import Stack


OPERANDI = "0123456789"


def u_postfixno(infixno):

    prioritet = {"^": 4,
                 "*": 3,
                 "/": 3,
                 "+": 2,
                 "-": 2,
                 "(": 1}
    
    
    lista_postfix = [ ]          # operandi idu na lisu
    operatori = Stack()         # operatori idu na Stek
    
    for znak in infixno:    
        if znak[0] in OPERANDI:
            lista_postfix.append(znak)
             
        elif znak == "(":       # leve zagrade --> Stek, desne --> brisu
            operatori.push(znak)
        
        # desne zagrade izbacuju sve sa steka dok ne naidje na levu zagradu
        elif znak == ")":
            poslednji = operatori.pop()
            while poslednji != "(":
                lista_postfix.append(poslednji)
                poslednji = operatori.pop()  
                
        #kada su operatori istog prioriteta onda se posednji izbacuje 
        else:
            while not operatori.is_empty() and prioritet[operatori.top()] >= prioritet[znak]:
                lista_postfix.append(operatori.pop())           #dodjaje el sa vrha steka
            operatori.push(znak)
            
     
    while not operatori.is_empty():
        lista_postfix.append(operatori.pop())
    
    return " ".join(lista_postfix)
            
    
    
            
if __name__ == '__main__':
    print (u_postfixno("2+3"))
    #print u_postfixno("22+3+4")
    """print u_postfixno('2+3')
    print u_postfixno('3+4*5/6')
    print u_postfixno("(7+8)/3+1")
    print u_postfixno('(7+8)/(3+2)')
    print u_postfixno('9*2-3+5')
    print u_postfixno('(4+8)*(6-5)/((3-2)*(2+2))')"""
