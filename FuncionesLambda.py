"""
2) Funciones Lambda

"""


# llamar n cantidad de veces una funcion f y aplicarla a x
cero = lambda f,x: x
uno = lambda f,x: (f)(x)
dos = lambda f,x: (f)(uno(f,x))
tres = lambda f,x: (f)(dos(f,x))


# aplicar funcion f, al parametro x, n+1 cantidad de veces
# aqui tengo que llamar recursivamente a sucesor, 
# modificar el contador en cada llamada
# verificar que el caso sea n == 0 

sucesor = lambda n,f,x: (f)(x) if n == 0 else sucesor(n-1,f,(f)(x)) 


# aritmetica
suma = lambda a,b,f,x: x
multiplicacion = lambda a,b,f,x: x
potencia = lambda a,b,f,x:x


# funciones de prueba
alfa = lambda x: x + 1
beta = lambda x: 2 * x


print()
# print(sucesor(10,beta,0))
print(sucesor(1,beta,3)) # al llamar a beta 1 vez retorna 12, ya que hace ((3 * 2) * 2), 
                         # lo cual es correcto ya que es ejecutarse n+1 veces
# print(sucesor(10,beta,1))
# print(sucesor(10,beta,2))
print()

print(sucesor(10,alfa,0)) # al llamar a alfa 10 veces, debe sumarle 11 veces 1
# print(sucesor(3,alfa,1))
# print(sucesor(3,alfa,2))