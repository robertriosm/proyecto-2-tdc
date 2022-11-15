
class Gramatica ():

    def __init__(self, V: set, T: set, S: str, P:list) -> None:
        """_summary_

        Args:
            V (set): Conjunto de variables o simbolos no terminales
            T (set): Conjunto de simbolos terminales
            S (_type_): Simbolo inicial
            P (list): Conjunto de reglas, espera tener una lista de sets; la gramatica supone que las reglas estan en la forma normal de Chomsky
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
        return False