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