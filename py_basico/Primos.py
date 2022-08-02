
def es_primo(numero):
    counter = 0
    for i in range(1, numero + 1):
        if i==1 or i == numero:
            continue
        if numero%i ==0:
            counter +=1
            break
    if counter == 0:
        return True
    else:
        return False

def run():
    numero = int(input("Digite un numero: "))
    if es_primo(numero):
        print('el numero '+str(numero)+' es primo')
    else:
        print("el numero "+str(numero)+" no es primo")


if __name__ == '__main__':
    run()
