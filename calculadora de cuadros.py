Largo = int(input("Ancho del cuadro en centimetros:"))
Ancho = int(input("Alto del cuadro en centimetros:"))
perfilA = 70
perfilB = perfilA*1.10
perfilC = 90
perfilD = perfilC*1.10
perfil = 0

selecperfil = input("Seleccione perfil del cuadro\n Opciones 1, 2, 3, o 4:")
perimetro = 2*Largo+2*Ancho

if selecperfil == 1:
    perfil = perfilA
if selecperfil == 2:
    perfil = perfilB
if selecperfil == 3:
    perfil = perfilC
if selecperfil == 4:
    perfil = perfilD


if Largo >= 70:
    costR1 = perfil
else:
    costR1 = 0

if Ancho >= 70:
    costR2 = perfil
else:
    costR2 = 0

costP = perimetro + perfil

TotalCost = costP + costR1 + costR2
print("Costo del cuadro: \n$", TotalCost)
