def divisior(num):
        divisiors = [i for i in range(1, num+1) if num % i == 0]
        return divisiors

def run():

    nume = input('Digite un numero: ')
    assert nume.isnumeric(), 'Debes ingresar un numero'
    print('Los divisores de '+str(nume)+' son '+str(divisior(int(nume))))
    print(""" EL PROGRAMA HA TERMINADO """)

if __name__ == '__main__':
    run() 