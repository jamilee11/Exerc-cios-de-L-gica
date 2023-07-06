# Precisamos imprimir um número para cada andar de um hotel 
# de 20 andares. Porém, o dono é supersticioso e optou por
# não ter um 13 andar.
# Escreva um código que imprima todos os números exceto o 
# número 13.
# Escreva mais dois códigos que resolvam o mesmo problema,
# mas dessa vez usando os outros dois tipos de laços de
# repetição aprendidos.
#Como desafio, imprima eles em forma decrescente(20, 19, 18...):

# Utilizando laço For range.
for a in range(20, 0, -1):
  if a != 13:
    print(f"Andar {a} ")

# Utilizando o laço While.
andares = 21
while andares > 1:
  andares-=1
  if andares == 13:
    continue
  print(f"Andar {andares}")

# Utilizando o laço While True com break e continue.
andar = 21
while True:
  andar-=1
  if andar == 13:
    continue
  print(f"Andar {andar}")
  if andar == 1:
    break

  
