
operacao= (input ("qual operacao deseja realizar(+,-,*,/)? ou \'s\' para sair \n"))

if operacao=='+' or operacao== "-" or operacao== "*" or operacao== "/":
a= int(input("digite o primeiro numero: "))
b= int(input ("digite o segundo numero: "))

if operacao=="+":
 resultado= a+b  

elif operacao == "-":
 resultado= a-b

elif operacao== "*":
 resultado= a*b

elif operacao== "/":
 resultado= a/b

elif operacao== "S" or operacao= "s":
    

else:
  print("Operação invalida")

print(resultado)

input("pressione enter")