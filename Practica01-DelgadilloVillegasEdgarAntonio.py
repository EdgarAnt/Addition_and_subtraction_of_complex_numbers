#Suma y resta de numeros complejos
#Edgar Antonio Delgadillo Villegas

class comp:
    pr = 0
    pimagi = 0

    def __init__(self, r, imag):
        self.pr = r
        self.pimagi = imag
    def muestra(self):
        if self.pimagi < 0:
            print(self.pr, self.pimagi, 'i')
        else:
            print(self.pr, ' + ', self.pimagi, 'i')
    #Setter
    def cambioR(self, r):
        self.pr=r
    def cambioI(self, imag):
        self.pimagi=imag
    #Getter
    def regresaR(self):
        return self.pr
    def regresaI(self):
        return self.pimagi

def suma(num1, num2):
        r = num1.pr + num2.pr
        i = num1.pimagi + num2.pimagi
        resultado=comp(r, i)
        resultado.muestra()

def resta(num1, num2):
    r = num1.pr - num2.pr
    i = num1.pimagi - num2.pimagi
    resultado = comp(r, i)
    resultado.muestra()


n1=comp(6, 7)
n2=comp(12, -10)
print("\nConjunto de numero suma")
n1.muestra()
print("\nConjunto de numero resta")
n2.muestra()
print("\nsuma de los dos conjuntos")
n3=suma(n1, n2)
print("\nresta de los dos conjuntos")
n3=resta(n1, n2)