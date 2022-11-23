def findTerminalProductions(productions):
    for prod in productions[1]:
        if prod[0]==1:
            return prod[1]
    return []

S = 'S'
w = 'a a a b b b    '
words = (lambda w : [word for word in w.split(' ') if not word=='']) (w)
pyramid = {}
P = [
    ('S', [(0, ('A', 'B')), (0, ('X', 'B'))], 0),
    ('T', [(0, ('A', 'B')), (0, ('X', 'B'))], 0),
    ('X', [(0, ('A', 'T'))], 0),
    ('A', [(1, ['a'])], 1),
    ('B', [(1, ['b'])], 1),
]
#Revisa que este en termianles
cont = 0
""" for n in range(len(words)+1):
    start = i
    end = i + n
    section = words[start:end]
    substrings = []            
    for i in range(n):
        for j in range(start+1, end):
            substrings.append(((words[start:j], (start, j)), (words[j:end], (j, end)))) """

step = 1
start = 0
end = start+1
n = len(words)
while step<=n:
    if start == n:
        start = 0
        step += 1
    end = start+step
    if step==1:
        not_terminals_related = []
        terminal = words[start]
        for production in P:
            if production[2]==1 or production[2]==2: #has terminal related
                terminal_productions = findTerminalProductions(production)
                if terminal_productions:
                    if terminal in terminal_productions:
                        not_terminals_related.append(production[0])
        pyramid[f'{start}-{end}'] = not_terminals_related
    else:
        not_terminals_related = []
        for j in range(start+1, end):
            first_section = pyramid.get(f'{start}-{j}')
            second_section = pyramid.get(f'{j}-{end}')
            if first_section and second_section:
                for nnT1 in first_section:
                    for nnT2 in second_section:
                        for production in P:
                            if production[2]==0 or production[2]==2: #has non-terminal related
                                for prod in production[1]:
                                    if prod[0]==0:
                                        if prod[1] == (nnT1, nnT2):
                                            not_terminals_related.append(production[0])
            pyramid[f'{start}-{end}'] = not_terminals_related
             
    start += 1
    if end==n:
        start = 0
        step += 1
        print(f'step = {step}')
print( False if not pyramid.get(f'0-{n}') else S in pyramid.get(f'0-{n}'))