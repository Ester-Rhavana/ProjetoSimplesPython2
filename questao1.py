print("Olá, seja bem-vindo a lojinha da Ester Reges!")
valor_produto=float(input("Por favor, digite o valor do produto:"))
quant=int(input("Por favor, digite a quantidade:"))
valor_final=valor_produto*quant
if  (valor_final<2500):
    print(f"Não há desconto a ser concedido, o valor final é de R${valor_final}.") #aqui não quis colcoar print do valor sem desconto e com desconto, para não ficar repetitivo.
elif(valor_final>=2500 and valor_final<6000):
    desconto= valor_final - (4/100*valor_final)
    print(f"O valor SEM desconto é de R${valor_final}")
    print(f"O valor COM desconto é de R${desconto}")
elif(valor_final>=6000 and valor_final<10000):
    desconto= valor_final - (7/100*valor_final)
    print(f"O valor SEM desconto é de R${valor_final}")
    print(f"O valor COM desconto é de R${desconto}")    
else:
    desconto= valor_final - (11/100*valor_final)
    print(f"O valor SEM desconto é de R${valor_final}")
    print(f"O valor COM desconto é de R${desconto}")    