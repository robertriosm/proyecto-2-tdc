from Gramatica import Gramatica
gram = Gramatica(
    V = {'S', 'NP', 'VP', 'PP', 'V', 'P', 'N', 'Det'}, 
    T = {'cooks', 'drinks', 'eats', 'cuts', 'he', 'she', 'in', 'with', 'cat', 'dog', 'beer', 'cake', 'juice', 'meat', 'soup', 'fork', 'knife', 'oven', 'spoon', 'a', 'the'}, 
    S = 'S', 
    P=[
        ('S', [(0, ('NP', 'VP'))], 0),
        ('VP', [(0, ('VP', 'PP')), (0, ('V', 'VP')), (1, ['cooks', 'drinks', 'eats', 'cuts'])], 2),
        ('PP', [(0, ('P', 'NP'))], 0),
        ('NP', [(0, ('Det', 'N')), (1, ['he', 'she'])], 2),
        ('V', [(1, ['cooks', 'drinks', 'eats', 'cuts'])], 1),
        ('P', [(1, ['in', 'with'])], 1),
        ('N', [(1, ['cat', 'dog', 'beer', 'cake', 'juice', 'meat', 'soup', 'fork', 'knife', 'oven', 'spoon'])], 1),
        ('Det', [(1, ['a', 'the'])], 1)
    ]) 
print(gram.testWord('he drinks with he'))