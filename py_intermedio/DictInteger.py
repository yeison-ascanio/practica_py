def ec():
    dict = {i:i**3 for i in range(1,101) if i%3 !=0}
    print(dict)
    
def rl3():
    dict = {i:i**0.5 for i in range(1,1001)}
    print(dict)
    
def run():
    rl3()

if __name__ == '__main__':
    run()