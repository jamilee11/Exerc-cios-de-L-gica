# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento
# que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome
# do usuário e a idade que completou, ou completará, no ano atual(2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema
# informará o erro e continuará perguntando até que um valor correto seja preenchido.

# Observação: a função matemática Math.log10() está sendo utilizada aqui para contar quantos dígitos
# a variável ano_nascimento possui, sem a necessidade de converter a variável de int 
# para String, para então usar a função len() para contar seus dígitos.

import math

nome = str(input("Informe o seu nome completo: "))
while True:
    try:
        ano_nascimento = int(input("Informe o ano do seu nascimento: "))
        qt_digitos = math.log10(ano_nascimento)+1 
        if qt_digitos < 4:
            print("O ano de nascimento precisa possuir 4 números!")
            continue
        elif ano_nascimento < 1922 or ano_nascimento > 2021:
            print("O ano de nascimento precisa ser entre 1922 e 2021.")
            continue
    except:
        print("Digite o ano do nascimento corretamente, apenas números!")
        continue
    break
idade = abs(ano_nascimento - 2022)
print(f"{nome}, você completa/completou {idade} anos de idade no ano de 2022.")

