def IndexValores(alvopar):
    for i in range(len(values)):
        for j in range(len(values)):
            if i!=j:
                soma = int(values[i]) + int(values[j])
                if soma == alvopar:
                    if j> i:
                        print([i,j])


numString = input("Digite o vetor separado por virgula: ")

values= numString.split(',')

alvo = input("Digite o alvo: ")

alvo = int(alvo)

IndexValores(alvo)



