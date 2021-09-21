# Izracunavanje aritmetickih izraza
from Stek import Stack

from Izracunavanje import izracunaj
from Postfixno import u_postfixno
import tokenizer


if __name__ == "__main__":
    print ("Izracunavanje aritmetickih izraza.")
    print ("**********************************")
    print
    pokrnuto = True
    while pokrnuto == True:
        izraz = input("Unesite izraz >> ")
        try:
            izraz = tokenizer.tokenize(izraz)
            print ("Ovo je izraz koji ste zadali:" , izraz)
            izraz = u_postfixno(izraz)
            print ("Izraz u postfiksnom obliku >>" , izraz)
            print
           
            izraz = izracunaj(izraz)
            print ("Rezultat >> ", izraz)
            print ("-----------")
        except Exception as e:
            print (e)
            print ("Najverovatnije da izraz koji ste uneli nije validan.")
