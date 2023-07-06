# Faça uma função calculadora de dois números com três paramêtros:
# os dois primeiros serão os números da operação e o terceiro será a 
# entrada que definirá a operação a ser executada, Considera a seguinte
# definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Caso seja inserido um número de operação que não exista, o resultado
# deverá ser 0 zero.

def calculadora(numero1, numero2, operacao):
    if operacao == 1:
        calculo = numero1 + numero2
        return calculo
    elif operacao == 2:
        calculo = numero1 - numero2
        return calculo
    elif operacao == 3:
        calculo = numero1 * numero2
        return calculo
    elif operacao == 4:
        calculo = numero1 // numero2
        return calculo
    else:
        return 0
        
print(calculadora(2, 56, 1))


