import math

# 1. Faça uma função que receba o nome de uma pessoa como entrada e retorne uma saudação.
# Exemplo:
# Boa tarde, Samuel. Seja bem vindo!
def saudacao(nome):
    mensagem = f"Boa tarde, {nome}. Seja bem vindo!"
    return mensagem

# 2. Faça uma função que peça o raio de um círculo e retorne sua área.

def area_circulo(raio):
    area = (raio**2)*math.pi
    return area

# 3. Faça uma função que converta a temperatura de Fahrenheit para Celsius.
# C = 5 * ((F-32) / 9).
def fahrenheit_para_celsius(far):
    celsius = ((far - 32)/9)*5
    return celsius

# 4. Faça uma função que calcule a multa por excesso de peso de peixes.
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma funçao que receba como
# entrada o peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# Exemplos de saidas para os parâmetros 70 e 25 respectivamente:
#
# Excesso de peso: 20 kg.
# Multa a pagar: R$ 80.00.
#
# Peso dentro do limite. Nenhuma multa aplicada.
def calculo_multa(peso):
    if peso > 50:
        excesso = peso - 50
        multa = (excesso)*4
        mensagem = f"Excesso de peso: {excesso} kg.\nMulta a pagar: R$ {multa}.00."
    else:
        mensagem = ("Peso dentro do limite. Nenhuma multa aplicada.")
    return mensagem    

# 5. Faça uma função para calcular a quantidade de tinta necessária para pintar uma área.
# O função deverá receber o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga no cálculo de litros necessários para cobrir
# a área a ser pintada e sempre arredonde os valores para cima,
# isto é, considere latas cheias.

## Exemplo de saída para uma área de 100 metros quadrados
# Quantidade de latas de 18L: 2
# Preço total: R$ 160.00
#
# Quantidade de galões de 3,6L: 6
# Preço total: R$ 150.00
#
# Quantidade de latas: 1, Quantidade de galões: 1
# Preço total: R$ 105.00
def calcular_tinta(area):
    litros = (area/6)*1.1
    quantlatas = math.ceil(litros/18)
    ql=quantlatas*80.00
    quantgaloes = math.ceil(litros/3.6)
    qg=quantgaloes*25.00
    mixlatas = math.floor(litros/18)
    mixgaloes = math.ceil((litros%18)/3.6)
    mix = mixlatas*80.00 + mixgaloes*25.00
    mensagem = f"Quantidade de latas de 18L: {quantlatas}\nPreço total: R$ {ql:.2f}\n\nQuantidade de galões de 3,6L: {quantgaloes}\nPreço total: R$ {qg:.2f}\n\nQuantidade de latas: {mixlatas}, Quantidade de galões: {mixgaloes}\nPreço total: R$ {mix:.2f}"
    return mensagem


# 6. Faça uma função que receba dois números e retorne o maior deles.
def maior_numero(valor1, valor2):
    if valor1>valor2:
        return valor1
    elif valor1<valor2:
        return valor2
    else:
        return valor1

# 7. Faça uma função que verifique se uma letra é vogal ou consoante.
def verificar_letra(letra):
    if (letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra == 'u'):
        return("Vogal")
    else:
        return("Consoante")    

# 8. Faça um Programa que receba três números e retorne o maior deles.
def maior_tres_numeros(num1, num2, num3):
    numeros = []
    numeros.append(num1)
    numeros.append(num2)
    numeros.append(num3)
    return max(numeros)

# 9. Faça uma função que retorne o menor valor entre três numeros informados.
def produto_mais_barato(num1, num2, num3):
    numeros = []
    numeros.append(num1)
    numeros.append(num2)
    numeros.append(num3)
    return min(numeros)

# 10. Faça uma funçao que retorne uma saudação com base no turno de estudo.
# A entrada deverá ser M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def saudacao_turno(turno):
    if turno == 'M':
        mensagem = "Bom Dia!"        
    elif turno == 'V':
        mensagem = "Boa Tarde!"  
    elif turno == 'N':
        mensagem = "Boa Noite"
    else:
        mensagem = "Valor Inválido!"
    return mensagem    
    

# 11. Faça uma função para um caixa eletrônico que informe quantas notas de cada valor serão fornecidas
# ao ser solicitado um saque.
# A função receberá como entrada o valor do saque e retornará quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo de saída para uma entrada de 346
# Notas fornecidas:
# 3 nota(s) de R$ 100
# 4 nota(s) de R$ 10
# 1 nota(s) de R$ 5
# 1 nota(s) de R$ 1

def caixa_eletronico(valor):
    quantnotas100 = 0
    quantnotas50 = 0
    quantnotas10 = 0
    quantnotas5 = 0
    quantnotas1 = 0
    if (valor >=10 and valor <=49):
        quantnotas100 = 0
        quantnotas50 = 0
        quantnotas10 = math.floor(valor/10)
        if (math.floor(valor%10)>=5):
            quantnotas5 = math.floor((valor%10)/5)
            quantnotas1 = math.floor((valor%10)%5)
        else:
              quantnotas5 = 0
              quantnotas1 = math.floor(valor%10)
    elif (valor >=50 and valor <=99):
        quantnotas100 = 0
        quantnotas50 = 1
        quantnotas10 = math.floor((valor%50)/10)
        if (math.floor((valor%50)%10)==5):
            quantnotas5 = math.floor((valor%50)%10/5)
        elif (math.floor((valor%50)%10)>5):
            quantnotas5 = math.floor((valor%50)%10/5)  
            quantnotas1 = math.floor(((valor%50)%10)%5)
        elif (math.floor((valor%50)%10)<5):
            quantnotas5 = 0
            quantnotas1 = math.floor((valor%50)%10)
    else:
        quantnotas100 = math.floor(valor/100)
        if (valor%100 > 0 and valor%100 <10):
            if math.floor(valor%100)<5:
                quantnotas1 = math.floor(valor%100)
            else:
                quantnotas5 = math.floor(valor%100/5)
                quantnotas1 = math.floor(valor%100%5)  
        elif (valor%100 >=10 and valor%100 <=49):
            quantnotas50 = 0
            quantnotas10 = math.floor(valor%100/10)
            if (math.floor(valor%100%10)>=5):
                quantnotas5 = math.floor((valor%100%10)/5)
                quantnotas1 = math.floor((valor%100%10)%5)
            else:
              quantnotas5 = 0
              quantnotas1 = math.floor(valor%100%10)
        elif (valor%100 >=50 and valor%100 <=99):
            quantnotas50 = 1
            quantnotas10 = math.floor((valor%100%50)/10)
            if (math.floor((valor%100%50)%10)==5):
                quantnotas5 = math.floor((valor%100%50)%10/5)
            elif (math.floor((valor%100%50)%10)>5):
                quantnotas5 = math.floor((valor%100%50)%10/5)  
                quantnotas1 = math.floor(((valor%100%50)%10)%5)
            elif (math.floor((valor%100%50)%10)<5):
                quantnotas5 = 0
                quantnotas1 = math.floor((valor%100%50)%10)
    if quantnotas10<1:
        mensagem = f"Notas fornecidas:\n{quantnotas100} nota(s) de R$ 100\n{quantnotas50} nota(s) de R$ 50\n{quantnotas5} nota(s) de R$ 5\n{quantnotas1} nota(s) de R$ 1\n"
    elif quantnotas1>0:
        mensagem = f"Notas fornecidas:\n{quantnotas100} nota(s) de R$ 100\n{quantnotas50} nota(s) de R$ 50\n{quantnotas10} nota(s) de R$ 10\n{quantnotas5} nota(s) de R$ 5\n{quantnotas1} nota(s) de R$ 1\n"    
    return mensagem


# 12. Desenvolva uma lógica que classifique uma pessoa com base nas respostas sobre um crime.
# A função deverá receber receba a resposta as seguintes perguntas:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
def classificar_participacao(questionario = ["perg1", "perg2", "perg3", "perg4", "perg5"]):
    afirmativo = questionario.count('sim')
    if afirmativo == 2:
        classificacao = "Suspeita"
    elif afirmativo == 3:
        classificacao = "Cúmplice"
    elif afirmativo == 4:
        classificacao = "Cúmplice"
    elif afirmativo == 5:
        classificacao = "Assassino"
    else:
        classificacao = "Inocente"     
    return classificacao               


# 13. Faça um Programa que calcule o preço da carne em uma promoção com desconto opcional.
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva uma função que receba o tipo e a quantidade de
# carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_preco_carne(tipo, quantidade, cartao):
    if quantidade > 5:
        if tipo=="File Duplo":
            if cartao == True:
                preco = 0.95(5.8*quantidade)
            else:
                preco = 5.8*quantidade
        elif tipo=="Alcatra":
            if cartao == True:
                preco = 0.95(6.8*quantidade)
            else:
                preco = 6.8*quantidade
        elif tipo=="Picanha":
            if cartao == True:
                preco = 0.95(7.8*quantidade)
            else:
                preco = 7.8*quantidade
    if quantidade <= 5:
        if tipo=="File Duplo":
            if cartao == True:
                preco = 0.95(4.9*quantidade)
            else:
                preco = 4.9*quantidade
        elif tipo=="Alcatra":
            if cartao == True:
                preco = 0.95(5.9*quantidade)
            else:
                preco = 5.9*quantidade
        elif tipo=="Picanha":
            if cartao == True:
                preco = 0.95(6.9*quantidade)
            else:
                preco = 6.9*quantidade   
    return preco                 

# 14. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.
def potencia(base, expoente):
    solucao = 1
    for i in range (1, expoente+1):
        solucao = solucao * base
    return solucao    

# 15. Faça um Programa que retorne o menor, maior e a soma de um conjunto de números.
def estatisticas_numeros(conjunto = []):
    return min(conjunto), max(conjunto), sum(conjunto)

# 16. Faça uma função que valide se uma nota está entre 0 e 10.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# Exemplos de saídas para as entradas -1 e 5.5 respectivamente:
# Erro: A nota deve estar entre 0 e 10. Tente novamente.
# Nota válida: 5.5

def validar_nota():
    pass
#    i=0
#    while i==0:
#        try:
#            nota=float(input())
#            if nota>=0.0 and nota<=10.9:
#                print("Nota válida: ", ("%.2f" % nota))
#                i=9
#            else:
#                print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
#        except:
#            print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")

# 17. Faça uma funçao que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
# Exemplos de saídas com as entradas "user" "user" "user123" respectivamente
# "Erro: A senha não pode ser igual ao nome de usuário. Tente novamente."
# "Usuário e senha cadastrados com sucesso!"
def validar_usuario_senha():
    user = input()
    while True:
        password = input()
        if password != user:
            break
        else:
            print('Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.')
    return 'Usuário e senha cadastrados com sucesso!'

# 18. Faça um Programa que calcule a média aritmética de um conjunto de N notas.
def media_notas(notas):
    media = sum(notas)/len(notas)
    return media

# 19. Faça um programa que mostre os n termos da Série a seguir:
#     S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
def calcular_serie(n):
    soma=1
    if n>1:
        for i in range (2, n+1):
            fator = i/(2*i - 1)
            soma+=fator
    return round(soma,2)    
        

# 20. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
#  A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: João Silva
# Nota: 7.9
# Nota: 8.5
# Nota: 9.4
# Nota: 7.0
# Nota: 8.8
# Nota: 9.8
# Nota: 7.9

# Resultado final:
# Atleta: João Silva
# Melhor nota: 9.8
# Pior nota: 7.0
# Média: 8.50
def calcular_media_ginastica(nome, notas=["nota1", "nota2", "nota3", "nota4", "nota5", "nota6", "nota7"]):
    notaAlta = -1
    notaBaixa = 11
    for i in range (7):
        if notas[i]>notaAlta:
            notaAlta=notas[i]
        if notas[i]<notaBaixa:
            notaBaixa=notas[i]    
    soma = sum(notas) - notaBaixa - notaAlta
    media = soma/5
    conclusao = f"Atleta: {nome}\nNota: {notas[0]}\nNota: {notas[1]}\nNota: {notas[2]}\nNota: {notas[3]}\nNota: {notas[4]}\nNota: {notas[5]}\nNota: {notas[6]}\n\nResultado final:\nAtleta: {nome}\nMelhor nota: {notaAlta}\nPior nota: {notaBaixa}\nMédia: {round(media, 2)}"
    return conclusao

# 21. Faça um Programa que desenhe uma pirâmide alinhada à esquerda.
def piramide_esquerda(n):
    y="#\n"
    for i in range (2, n+1):
        x="#"
        y = y + (f"{x*i}\n")
    return y

# 22. Faça um Programa que desenhe uma pirâmide alinhada à direita.
def piramide_direita(n):
    r = ""
    y=n-1
    for i in range (1, n+1):
        x="#"
        z=" "
        r = r + (y*(z)) + (f"{x*i}\n")
        y-=1
    return r

# 23. Faça um Programa que desenhe duas pirâmides lado a lado.
def piramides_lado_a_lado(n):
    r = ""
    y=n-1
    for i in range (1, n+1):
        x="#"
        z=" "
        r = r + (y*(z)) + (f"{x*i} ") + (f"{x*i}\n")
        y-=1
    return r

# 24. Faça um Programa que calcule o troco com a menor quantidade de moedas possível.
def calcular_troco(valor):
    quantmoedas50=0
    quantmoedas25=0
    quantmoedas10=0
    quantmoedas5=0
    quantmoedas1=0
    troco={}
    if valor>=50:
        while valor >= 50:
            valor = valor - 50
            quantmoedas50+=1
    if valor>=25:
        while valor >= 25:
            valor = valor - 25
            quantmoedas25+=1
    if valor>=10:
        while valor >= 10:
            valor = valor - 10
            quantmoedas10+=1
    if valor>=5:
        while valor >= 5:
            valor = valor - 5
            quantmoedas5+=1
    if valor>=1:
        while valor >= 1:
            valor = valor - 1
            quantmoedas1+=1
    if quantmoedas50>0:
        troco.update({50: quantmoedas50})
    if quantmoedas25>0:
        troco.update({25: quantmoedas25})
    if quantmoedas10>0:
        troco.update({10: quantmoedas10})
    if quantmoedas5>0:
        troco.update({5: quantmoedas5})
    if quantmoedas1>0:
        troco.update({1: quantmoedas1})
    return troco                              

# 25. Faça um Programa que valide um número de cartão de crédito usando o algoritmo de Luhn.
def validar_cartao(numero):
    soma=0
    num=str(numero)
    comprimento=len(num)
    i=comprimento-2
    contador=3
    
    while i>=-1:
        parcela = num[i+1]
        parc=int(parcela)
        if contador%2==0:
            parc*=2
        if parc > 9:
            p=str(parc)
            res = sum(int(j) for j in p)
            soma = soma + res
        elif parc<=9:
            soma = soma + parc
        i-=1
        contador+=1
    if soma%10==0 and num[0] == "5":
        resultado="Cartão Válido - Bandeira: MasterCard"
    elif soma%10==0 and num[0] == "4":
        resultado="Cartão Válido - Bandeira: Visa"
    elif soma%10==0 and num[0] == "3":
        resultado="Cartão Válido - Bandeira: American Express"
    elif soma%10!=0:
        resultado="Número inválido."
    else:
        resultado="Bandeira não reconhecida."
    return resultado