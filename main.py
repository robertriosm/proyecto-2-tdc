from Gramatica import Gramatica
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
print(gram.testWord('She eats a cake with a fork'))