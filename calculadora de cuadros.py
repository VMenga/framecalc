Largo = input("Ancho del cuadro en centimetros:")
Ancho = input("Alto del cuadro en centimetros")
perfilA = 70
perfilB = perfilA*1.10
perfilC = 90
perfilD = perfilC*1.10

selecperfil = input("Seleccione perfil del cuadro\n Opciones 1, 2, 3, o 4:")
perimetro = 2*Largo+2*Ancho

def switch_perfil(selecperfil):
    perfil = {
    1: perfilA,
    2: perfilB,
    3: perfilC,
    4: perfilD,
    }
    perfil = switch_perfil.get(selecperfil)
    return perfil()

costP = perimetro * perfil

if Largo >= 70:
    costR1 = perfil
else:
    costR1 = 0

if Ancho >= 70:
    costR2 = perfil
else:
    costR2 = 0

TotalCost = CostP+CostR1+CostR2
print("Costo del cuadro \n$", TotalCost)
