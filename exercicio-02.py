def funcao(nome1,nome2):
    teste3=1
    valor1=len(nome1)+1
    valor2=len(nome2)+1
    if valor1==valor2:
        for i in range(1,valor1):
            contador=i*-1
            teste1=nome1[contador]
            teste2=nome2[i-1]
            if teste2==teste1:
                teste3=teste3+1
        if teste3==valor1:
            print("As palavras são iguais")
        else:
            print("As palavras são diferentes")
    else:
        print("As palavras são diferentes")

palavra1=input("Insira uma palavra ")
palavra2=input("Insira uma palavra reversa ")
funcao(nome1=palavra1,nome2=palavra2)