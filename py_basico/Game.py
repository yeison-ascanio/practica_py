import random
def looking_number():
    num = random.randint(0, 100)
    while(True):
        numero = int(input('Elige un numero del 1 al 100: '))
        if numero<num:
            print('Busca un numero mas grande.')
        elif numero>num:
            print('Busca un numero mas chico')
        else:
            print("Ganaste!")
            break
            
            
def run():
    looking_number()

if __name__ == '__main__':
    run()