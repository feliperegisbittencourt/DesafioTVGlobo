def maxLucro(data):
    lucro = 0

    for i in range(len(data)):
        maior = data[0]
        maiorId = 0
        menor = data[0]
        menorId = 0
        if data[i]>maior:
            maior = data[i]
            maiorId = i
        if(data[i]<menor):
            menor = data[i]
            menorId = i

    if maiorId > menorId:
        lucro = maior - menor
    else:
        if(data[menorId+1] - data[menorId] > data[maiorId] - data[maiorId-1]):
            data.pop(maiorId)
            maxLucro(data)
        else:
            data.pop(menorId)
            maxLucro(data)


    print(lucro)


dados = input("Digite a lista de preços separados por virgula: ")

dadosSplit = dados.split(',')
maxLucro(dadosSplit)