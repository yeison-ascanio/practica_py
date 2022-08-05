def read():
    numbers = []
    with open("py_intermedio/Files/data.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers) 
# terminar el codigo, añadir un sistema que seleccione un elemento, luego que por cada caracter digitado revise si es igual a la palabra que eligio
# y lo escriba en pantalla

def run():
    read()

if __name__ == '__main__':
    run()