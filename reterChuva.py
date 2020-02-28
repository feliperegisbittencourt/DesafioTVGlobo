def reter(data):
    atual = 0
    reter = 0
    anterior = atual - 1
    proximo = atual + 1
    antes = atual - 2
    depois = atual + 2
    reterAntes = False
    reterDepois = False

    for i in range(len(data)):
        atual = i
        if i != 0 or i != len(data) -1:
            if countAntes !=0:
                reterAntes = False
            if countDepois !=0:
                reterDepois = False
            if reterAntes and reterDepois:
                reter +=1
                reterAntes = False
                reterDepois = False
            if data[i] < data[anterior] and data[i] < data[proximo]:
                reter += 1
            if data[i] < data[antes] and data[anterior] < data[antes]:
                reter += 1
                reterAntes = True
                countAntes = 0
            if data[i] < data[depois] and data[proximo] < data[depois]:
                reter += 1
                reterDepois = True
                countDepois = 0
            countAntes +=1
            countDepois +=1
        print(reter)


dados = input("Digite a elevação do terreno separado por virgula: ")
dadosSplit = dados.split(",")
reter(dadosSplit)
            