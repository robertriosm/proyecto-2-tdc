from Gramatica import Gramatica
from FuncionesLambda import *
gram = Gramatica(
    V = {'S', 'A', 'B', 'C', 'V', 'P', 'N', 'D'}, 
    T = {'cooks', 'drinks', 'eats', 'cuts', 'he', 'she', 'in', 'with', 'cat', 'dog', 'beer', 'cake', 'juice', 'meat', 'soup', 'fork', 'knife', 'oven', 'spoon', 'a', 'the'}, 
    S = 'S', 
    P=[
        ('S', [(0, ('A', 'B'))], 0),
        ('B', [(0, ('B', 'C')), (0, ('V', 'A')), (1, ['cooks', 'drinks', 'eats', 'cuts'])], 2),
        ('C', [(0, ('P', 'A'))], 0),
        ('A', [(0, ('D', 'N')), (1, ['he', 'she'])], 2),
        ('V', [(1, ['cooks', 'drinks', 'eats', 'cuts'])], 1),
        ('P', [(1, ['in', 'with'])], 1),
        ('N', [(1, ['cat', 'dog', 'beer', 'cake', 'juice', 'meat', 'soup', 'fork', 'knife', 'oven', 'spoon'])], 1),
        ('D', [(1, ['a', 'the'])], 1)
    ]) 
exit = False
inciso2= funcionesLambda()
while not exit:
    inpt = input('------Proyecto 2------\n1. Probar palabra en gramatica\n2. Inciso funciones Lambda2\n3. Salir\n')
    if inpt == '1':
        w = input('Ingrese frase: ')
        ret = gram.testWord(w)
        print(('\nSi' if ret[0] else '\nNo') + f' pertenece al lenguaje de la gramatica.\nTiempo en simluación: {ret[1]}')
        input("\nEnter para regresar al menu principal...")
    elif inpt == '2':
        inciso2.funciones()
    elif inpt == '3': exit = True
    else:
        print("Ingrese una opción válida")