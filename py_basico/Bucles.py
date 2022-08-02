def potenciaMil(numero):
    i = 0
    while(True):
        if(i**numero>100000):
            break
        else:
            print('el mumero '+str(i)+' elevado a '+str(numero)+' = '+str(i**numero), "\n")
            i += 1
        

def run():
    numero = int(input("Digite una potencia: "))
    potenciaMil(numero)


if __name__ == '__main__':
    run()