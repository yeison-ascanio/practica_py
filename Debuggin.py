def divisior(num):
        divisiors = [i for i in range(1, num+1) if num % i == 0]
        return divisiors

def run():
    try:
        nume = int(input('Digite un numero: '))
        try:
            if nume < 0:
                raise ValueError('No se pueden ingresar numeros negativos')
            print('Los divisores de '+str(nume)+' son '+str(divisior(nume)))
            print(""" EL PROGRAMA HA TERMINADO """)
        except ValueError as ve:
            print(ve)

    except ValueError:
        print('Debes ingresar un numero valido.')

if __name__ == '__main__':
    run() 