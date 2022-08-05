# primeros 100 numeros naturales al cuadrado
def raiser():
    llist = [i**2 for i in range(1,101) if i%3 !=0]
    # for i in range(1,101):
    #     if i%3 !=0:
    #         llist.append(i**2)
    squares = [ i for i in range(1, 100000) if i % 36 == 0]
    print(squares)
    # print(llist)

def run():
    raiser()

if __name__ == '__main__':
    run()