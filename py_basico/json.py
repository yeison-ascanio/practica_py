from curses import keyname
from pip import main


def run():
    dic = {
        'serval' : ['yeison', 'ivan', 'andres', 'jesus', 'sarai', 'cesar'],
        'soporte':['francisco', 'orlando', 'chicago']
    }
    
    for team, collabs in dic.items():
        print('equipo '+team+' tiene colaboradores que son los siguientes: '+str(collabs.values()))

if __name__ == '__main__':
    run()