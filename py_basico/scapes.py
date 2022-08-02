def run():
    print("""
    ***********************
          BIENVENIDO
    ***********************""")
    while(True):
        palabra = input('Digite la palabra secreta: ')
        if palabra.lower() == 'python':
            print(
                """
            *********************************************************************
                FELICITACIONES, HAZ DESCUBIERTO LA PALABRA SECERETA
            *********************************************************************"""
            )
            break
        else:
            print('\nError, la palabra '+palabra+' no es correcta\n')

if __name__ == '__main__':
    run()