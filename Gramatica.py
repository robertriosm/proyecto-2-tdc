
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
        def findTerminalProductions(productions):
            for prod in productions[1]:
                if prod[0]==1:
                    return prod[1]
            return []

        words = (lambda w : [word.lower() for word in w.split(' ') if not word=='']) (w)
        pyramid = {}
        #Revisa que este en termianles
        for word in words: 
            if word not in self.T: 
                return False
        
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
                                for production in self.P:
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
        return False if not pyramid.get(f'0-{n}') else self.S in pyramid.get(f'0-{n}')