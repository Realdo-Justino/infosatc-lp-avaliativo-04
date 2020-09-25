def funcao(nome):
    valor=len(nome)+1
    for i in range(1,valor):
        contador=i*-1
        print(nome[contador])
palavra=input("Insira uma palavra ")
funcao(palavra)