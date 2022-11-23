from time import time 


class Gramatica ():

    def __init__(self, V: set, T: set, S: str, P:list) -> None:
        """_summary_

        Args:
            V (set): Conjunto de variables o simbolos no terminales
            T (set): Conjunto de simbolos terminales
            S (_type_): Simbolo inicial
            P (list): Conjunto de reglas, espera tener una lista de sets; 0: Tiene el lado izq. de la produccion, 1: contiene el lado derecho de la produccion en forma de lista, considerando or's, esta lista a su vez contiene sets que tiene por primera posicion el tipo de produccion (a terminales o no terminales) y la segunda la produccion en si. 2: (2) Tiene producciones a no terminales y a terminales, (1) contiene producciones a terminales unicamente, (0) contiene producciones a no terminales solamente. 
        """
        self.V: set = V
        self.T: set = T
        self.S: str = S
        self.P: list = P        


    def testWord(self, w) -> bool:
        """Utilizando el algoritmo CYK indica si la frase pertenece a la gramatica. 

        Args:
            w (_type_): frase que se testea pertenece a la gramatica
        """

        words = (lambda w : [word.lower() for word in w.split(' ') if not word=='']) (w)
        pyramid = {}
        #Revisa que este en termianles
        start_simulation = time()
        for word in words: 
            if word not in self.T: 
                return False,  time()-start_simulation
        start_simulation = time()
       
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
                for production in self.P:
                    if production[2]==1 or production[2]==2: #has terminal related
                        for prod in production[1]:
                            if prod[0] == 1:
                                if terminal in prod[1]:
                                    not_terminals_related.append((production[0], terminal))
                pyramid[f'{start}-{end}'] = not_terminals_related
            else:
                not_terminals_related = []
                for j in range(start+1, end):
                    first_section = pyramid.get(f'{start}-{j}')
                    second_section = pyramid.get(f'{j}-{end}')
                    if first_section and second_section:
                        first_section =  [r[0] for r in first_section]
                        second_section = [r[0] for r in second_section]
                        for nnT1 in first_section:
                            for nnT2 in second_section:
                                for production in self.P:
                                    if production[2]==0 or production[2]==2: #has non-terminal related
                                        for prod in production[1]:
                                            if prod[0]==0:
                                                if prod[1] == (nnT1, nnT2):
                                                    not_terminals_related.append((production[0], ((f'{start}-{j}', nnT1), (f'{j}-{end}', nnT2))))
                    pyramid[f'{start}-{end}'] = not_terminals_related

            start += 1
            if end==n:
                start = 0
                step += 1
        accepted = False
        end_sim = time()
        for i in pyramid.get(f'0-{n}'):
            if not accepted and i[0]==self.S:
                accepted = True
        
        if accepted: #parse tree
            tree_describe = [(i, 0) for i in pyramid.get(f'0-{n}') if i[0]==self.S]

            while tree_describe:
                item = tree_describe.pop(0)
                lvl = item[1]
                item = item[0]
                left_side = item[0]
                right_side = ''

                if type(item[1]) is str:
                    right_side = item[1]
                else:
                    sucesores = item[1]
                    for i in range(len(sucesores)):
                        tree_describe.extend([(j, lvl+1,) for j in pyramid.get(sucesores[i][0]) if j[0]==sucesores[i][1]])
                        right_side += f'{sucesores[i][1]}'
                for k in range(lvl):
                    print("\t", end='')
                print(f'{left_side}-> {right_side}')

            
        return accepted,  end_sim - start_simulation 