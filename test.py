import libreria_complejos as cpmx

def printcomplex(c):
    if type(c) == float:
        print(round(c,2))
    else:
        if c[1] < 0:
            return (str(c[0]) + " - " + str(abs(c[1])) + "i")
        else:
            return (str(c[0]) + " + " + str(c[1]) + "i")


def casos_prueba(rest1,ver1,rest2,ver2):
    Passed = 0
    Failed = 0
    if rest1 == ver1:
        Passed+=1
    else:
        Failed+=1
    if rest2 == ver2:
        Passed+=1
    else:
        Failed+=1

    return "De dos casos pruebas:",Passed, "Pasaron con exito y",Failed,"No funcionaron con exito" 
  

c1 = (2,5)
c2 = (7,8)
c3 = (-21,15)
c4 = (-2,-2)

print("Suma")
val1 = cpmx.sumcomplex(c1,c2)
val2 = cpmx.sumcomplex(c3,c4)
print(*casos_prueba(val1,(9,13),val2,(-23,13)))
print()

print("Resta")
val1 = cpmx.restcomplex(c1,c2)
val2 = cpmx.restcomplex(c3,c4)
print(*casos_prueba(val1,(-5,-3),val2,(-19,17)))
print()

print("Multiplicación")
val1 = cpmx.multcomplex(c1,c2)
val2 = cpmx.multcomplex(c3,c4)
print(*casos_prueba(val1,(-26,51),val2,(72,12)))
print()

print("División")
val1 = cpmx.divcomplex(c1,c2)
val2 = cpmx.divcomplex(c3,c4)
print(*casos_prueba(val1,(0.48,0.17),val2,(1.5,-9.0)))
print()

print("Modulo")
val1 = cpmx.moducomplex(c1)
val2 = cpmx.moducomplex(c3)
print(*casos_prueba(val1,(5.39),val2,(25.81)))
print()

print("Conjugado")
val1 = cpmx.conjucomplex(c1)
val2 = cpmx.conjucomplex(c3)
print(*casos_prueba(val1,(2,-5),val2,(-21,-15)))
print()

print("Cartesiano a Polar")
val1 = cpmx.cartesian_to_polar_complex(c1)
val2 = cpmx.cartesian_to_polar_complex(c3)
print(*casos_prueba(val1,(5.39,1),val2,(25.81,3)))
print()

print("Fase")
val1 = cpmx.fasecomplex(c1)
val2 = cpmx.fasecomplex(c3)
print(*casos_prueba(val1,1.19,val2,2.52))
print()