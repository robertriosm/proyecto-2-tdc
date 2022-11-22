cero = lambda a: lambda x:x
uno = lambda a: lambda x:a(x)
dos = lambda a: lambda x:a(a(x))
tres = lambda a: lambda x:a(a(a(x)))

sucesor= lambda a: lambda b: lambda c: b(a(b)(c))
suma = lambda d: lambda e: lambda f: lambda g: d(f)(e(f)(g))
multiplicacion = lambda n: lambda f: lambda x: lambda y: n(f(x))(y)
potencia = lambda a: lambda b: lambda c: lambda d: b(a)(c)(d)

alfa = lambda a: a + 1
beta = lambda a: 2 * a