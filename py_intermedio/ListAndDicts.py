from traceback import print_tb


def iterator(val):
    for key, value in val.items():
        print(key, ' - ', value)


def iteratorList(val):
    for value in val:
       for key,values in value.items():
        print(f'{key} - {value}')


def run():
    myList = [1, 'hola', True, 4, 5]
    myDict = {'serval': 'backend', 'heaven': 'frontend'}

    super_list = [
        {'dulce': 'cocosete', 'helado': 'cream helado'},
        {'modelo': '12', 'marca': 'redmi'},
        {'firstName': 'ivan', 'pseudonimo': 'paraco'},
        {'tipoContrato': 'undefine'},
        {'skill': 'fast learning', 'actitude': 'winner'}
    ]
    super_dict = {
        'naturalNumber': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        'integerNumber': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        'floatNumber': [1.2, 1.1, 1.5, 2.1, 2.5, 3.5, 6.8, 9.8]
    }

    iterator(super_dict)
    iteratorList(super_list)


if __name__ == '__main__':
    run()
