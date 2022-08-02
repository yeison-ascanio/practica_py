def conver(valor_dolar):
    pesos = float(input("Cuanto dinero tienes?: "))
    return print("Tienes $"+str(round(pesos/valor_dolar,2))+" dolares.")

while True:
    word = input("""Que tipo de mondeda tiene: 
    1. colombiana.
    2. mexicana.
    3. bolivares.""").lower()
    if word == '1':
        conver(4400)
        break
    if word == '2': 
        conver(27)
        break
    if word == '3':
        conver(345678345)
        break
    if word != '1' or word != '2':
        break

