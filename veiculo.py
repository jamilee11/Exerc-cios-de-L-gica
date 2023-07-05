#Desenvolva um código que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#Com essas informações, o programa mostrará qual é a melhor 
#categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e 
#seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
#E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

#Minha resolução do exercício na Linguagem Python.


qt_rodas = int(input("Quantidade de rodas: "))
peso_bruto = int(input("Capacidade de transporte: "))
qt_pessoas = int(input("Quantidade de pessoas: "))

if qt_rodas == 2 or qt_rodas == 3:
    print("Categoria A")
elif qt_rodas == 4 and qt_pessoas <= 8 and peso_bruto <= 3500:
    print("Categoira B")
elif qt_rodas >= 4 and peso_bruto >= 3500 and peso_bruto <= 6000:
    print("Categoria C")
elif qt_rodas >= 4 and qt_pessoas >= 8:
    print("Categoria D")
elif qt_rodas >= 4 and peso_bruto >= 6000:
    print("Categoria E")