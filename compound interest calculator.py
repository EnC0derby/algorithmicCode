t = 0
Value_Initial = float(input("write the bravery initial: R$")) #Aqui ele pedi o valor que ja voce ja possui
monthly_deposit = float(input("Monthly deposit R$")) # Aqui pergunta o deposito mensal
months = int(input("write the months: ")) #Aqui pede o tempo em meses que voce ira investir
dividend = float(input("write percentage dividend: %")) #Aqui ele pergunta a taxa de juros da ação

value_not = Value_Initial # Aqui  ele copia o valor inicial para a variavel value_not

while(t!=months): # Cria um condição para o loop, enquanto t for menor que os meses continua o loop
    p = dividend / 100 # Aqui ele pega o valor do divendo e divid por 100 
    Value_Initial = Value_Initial + monthly_deposit # Aqui ele soma o deposito mensal com o valor inicial
    Value_Initial = Value_Initial+(Value_Initial*p) # aqui ele soma o valor inicial com valor inicial mutilplicado pela variavel p e joga na varial de valor inicial

    value_not = value_not + monthly_deposit #  Aqui o value_not recebe a soma de valor inicial com o valor de deposito
    
    t = t+1

value = Value_Initial - value_not # Aqui ele decobre a diferença da soma dos meses com juros e sem juros, para saber quanto foi o ganho no tempo corrido
print("You will have: R$%.2f"%Value_Initial) # Escreve o valor total após o tempo corrido
print("monthly interest: R$%.2f"%value) # Escreve o ganho ao longo do tempo corrido