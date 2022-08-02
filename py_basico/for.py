def run(nombre):
    for num in range(11):
        print("10 * "+str(num)+' = '+str(num*10))
        
    nombre = input("Digite su nombre: ")
    for caracter in nombre:
        print(caracter)
        
if __name__ == '__main__':
    run()