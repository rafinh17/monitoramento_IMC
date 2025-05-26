#Receber o peso e a altura do usuário, calcular o IMC e exibir:
#O valor calculado
#Uma mensagem de orientação baseada no resultado
#O usuário informa o peso (kg) e a altura (m).
#O programa calcula o IMC:
nome = input('digite o nome do usuario :')
usuario_peso = float(input('digite o peso do usuario:'))
usuario_altura = float(input('digite a altura do usuario:'))
#O programa calcula o IMC:
IMC = usuario_peso / (usuario_altura ** 2)
#IMC >= 30.0 
#print ("Cuidado com a Saúde")
#IMC < 30.0 
#print ( "Tudo ok")

if IMC <=  18.5 :
    print("Abaixo do peso")
elif 18.5 < IMC < 24.9: 
    print("Peso normal")
elif 25.0  <= IMC < 29.9:
    print("Sobrepeso")
elif 30.0  <= IMC < 34.9:
    print("Obesidade Grau I")
elif 35.0  <= IMC <= 39.9 :
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III (mórbida)")
