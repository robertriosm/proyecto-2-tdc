"""
2) Funciones Lambda


Otra referencia general para comprender los numeros de church: https://www.youtube.com/watch?v=pAnLQ9jwprint_lambda-E
"""


# llamar n cantidad de veces una funcion f y aplicarla a x
cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))


# aplicar funcion f, al parametro x, n+1 cantidad de veces: SUCC:= λ n f x. f ((n f) x)
# sucesor = lambda n,f,x: (f)(x) if n == 0 else sucesor(n-1,f,(f)(x)) 
sucesor = lambda a: lambda f: lambda x: f(a(f)(x))


# aritmetica
# Referencias: https://es.wikipedia.org/wiki/C%C3%A1lculo_lambda


# La suma se define así: PLUS:= λ m n f x. n f (m f x)
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))


# La Multiplicación se expresa como MULT:= λ m n. m (PLUS n) 0
multiplicar = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)


# la potencia deberia ser, ejecutar sobre a, b veces la multiplicacion: a(b)(f)(x) = a**b(f)(x). 
potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)


# funciones de prueba
alfa = lambda x: x + 1
beta = lambda x: 2 * x


# se necesita poder ver el resultado de las funciones lambda
# Referencias: https://stackoverflow.com/questions/67552413/printing-of-a-function-or-lambda
def print_lambda(f): 
    try: name = [k for k,v in globals().items() if v == f][0]
    except: return f
    return '%s: %s' % (name, f)



print()
print("cero: ", print_lambda(cero(alfa)(0)))
print("uno: ", print_lambda(uno(alfa)(0)))
print("dos: ", print_lambda(dos(alfa)(0)))
print("tres: ", print_lambda(tres(alfa)(0)))
print("sucesor: ", print_lambda(sucesor(tres)(alfa)(0)))
print("suma: ", print_lambda(suma(dos)(tres)(alfa)(0)))
print("multiplicar: ", print_lambda(multiplicar(dos)(tres)(alfa)(0)))
print("potencia: ", print_lambda(potencia(dos)(tres)(alfa)(0)))

print()
print("cero: ", print_lambda(cero(beta)(0)))
print("uno: ", print_lambda(uno(beta)(1)))
print("dos: ", print_lambda(dos(beta)(1)))
print("tres: ", print_lambda(tres(beta)(1)))
print("sucesor: ", print_lambda(sucesor(tres)(beta)(1)))
print("suma: ", print_lambda(suma(dos)(tres)(beta)(1)))
print("multiplicar: ", print_lambda(multiplicar(dos)(tres)(beta)(1)))
print("potencia: ", print_lambda(potencia(dos)(tres)(beta)(1)))
