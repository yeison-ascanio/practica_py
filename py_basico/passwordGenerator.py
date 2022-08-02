from email import generator
import random
def generator_pass():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    mins  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    nums  = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    char  = ['*', '+', '-', '/', '@', '_', '?', '!', 'ß', 'π', '¶', 'ø', '}', '≈', ',', ';', '.', '>', '<', '~', '∞', '^', '&', '$', '#','≥','≤','≠','æ','¢']
    character = mayus+mins+nums+char
    passw = []
    po = """" 

    """
    for i in range(15):
        char_rand = random.choice(character)
        passw.append(char_rand)
        
    return ''.join(passw)

def run():
    password = generator_pass()
    print("La constraseña generada es : "+password)

if __name__ == '__main__':
    run()