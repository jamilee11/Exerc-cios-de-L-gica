# Faça uma função calculadora que os números e as operações serão
# feitas pelo usuário. O código  deve ficar rodando infinitamente até
# que o usuário escolha a opção de sair. No início, o programa mostará
# a seguinte lista de operações:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# 0. Sair
# Digite o número para a operação correspondente e caso o usuário
# introduza qualquer outro, o sistema deve mostrar a mensagem 
# "Essa opção não existe" e voltar ao menu de opções.
# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro
# e o segundo valor, um de cada. Depois precisa executar a operação e
# mostrar o resultado na tela. Quando o usuário escolher a opção "Sair",
# o sistema irá parar.
# É necessário que o sistema mostre as opções sempre que finalizar 
# uma operação e mostrar o resultado.

# Minha resolução do exercício. 
def calculadora(operacao, numero1, numero2):
    if operacao == 1:
        calculo = numero1 + numero2
        return calculo
    elif operacao == 2:
        calculo = abs(numero1 - numero2)
        return calculo
    elif operacao == 3:
        calculo = numero1 * numero2
        return calculo
    elif operacao == 4:
        calculo = numero1 // numero2
        return calculo

while True:
    print("-="*13)
    print("     Menu de opções")
    print("-="*13)
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    opcao = int(input("Digite a opção que você quer escolher: "))
    if opcao > 4:
        print("Essa opção não existe!")
        continue
    elif opcao == 0:
       break
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print(calculadora(opcao, valor1, valor2))





