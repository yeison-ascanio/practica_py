def read():
    numbers = []
    with open("py_intermedio/Files/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers) 
           
def writte():
    names = ['ivan','jesus','sarai','cesar','andres','yeison','bruno']
    with open("py_intermedio/Files/names.txt","a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    writte()

if __name__ == '__main__':
    run()