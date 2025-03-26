def validar_cartao(numero):
    soma=0
    num=str(numero)
    comprimento=len(num)
    i=comprimento-2
    contador=3
    if comprimento == 15:
        while i>=-1:
            parcela = num[i+1]
            parc=int(parcela)
            p=str(parc)
            j=i%2
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
        print(res)
validar_cartao(378282246310005)            