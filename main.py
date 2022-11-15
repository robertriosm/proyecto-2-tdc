from Gramatica import Gramatica
gram = Gramatica(
    V = {'S', 'NP', 'VP', 'PP', 'V', 'P', 'N', 'Det'}, 
    T = {'cooks', 'drinks', 'eats', 'cuts', 'he', 'she', 'in', 'with', 'cat', 'dog', 'beer', 'cake', 'juice', 'meat', 'soup', 'fork', 'knife', 'oven', 'spoon', 'a', 'the'}, 
    S = 'S', 
    P=[
        ('S', ('NP', 'VP'), 0),
        ('VP', ('VP', 'PP'), 0),
        ('VP', ('V', 'VP'), 0),
        ('VP', ['cooks', 'drinks', 'eats', 'cuts'], 1),
        ('PP', ('P', 'NP'), 0),
    ])