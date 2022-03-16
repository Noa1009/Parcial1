numeroValidar = int(input("Numero a validar: "))
contador = 0
lista1 = []
if numeroValidar < 0:
  print("Digite un numero positivo")
for inteligente in range(1,numeroValidar+1):
    if (numeroValidar % inteligente) == 0 :
        contador += 1
        lista1.append(inteligente)
print(lista1)
if len(lista1) > 2:
  print("el numero",numeroValidar,"si es inteligente")
elif len(lista1) <= 2:
    print("el numero",numeroValidar,"no es inteligente")