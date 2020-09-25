nome=[]
cpf=[]
senha=[]
apto=[]


def funcaoUsuarios(x,y,nome,cpf,senha,apto):
    print("")
    print("O nome do usuario ",x," é ",nome[y])
    print("O cpf do usuario ",x," é ",cpf[y])
    print("A senha do usuario ",x," é ",senha[y])
    print("O usuario ",x," esta apto? ",apto[y])

def cadastro():
    nome.append(input("Insira o seu nome"))
    cpf.append(input("Insira o seu cpf"))
    senha.append(input("Insira o seu senha"))
    apto.append(input("Insira o seu apto"))

pessoa=(int(input("Quantas pessoas vão fazer o teste para doar sangue: ")))
for x in range(pessoa):
    
    texto=""
    print("")
    usuario=0
    variavel=0
    idade=(int(input("Insira a sua idade: ")))
    peso=(float(input("Insira o seu peso: ")))
    tempo=(float(input("Insira quantas horas de sono tiveste na ultima noite: ")))
    if idade>16 and idade<69:
        variavel=variavel+1
    else:
        texto="idade "+texto
    if peso>50:
        variavel=variavel+1
    else:
        texto="peso "+texto
    if tempo>6:
        variavel=variavel+1
    else:
        texto="sono "+texto

    if variavel==3:
        print("Pode doar sangue")
        alternativa=(input("Deseja se cadastrar?(s/n): "))
        if(alternativa=="s"):
            usuario=usuario+1
            cadastro()

        else:
            pass
    else:
        print("Não pode doar sangue pois não atingiu o experado nas categorias de:",texto)

for x in range(usuario):
    contador=x+1
    funcaoUsuarios(contador,x,nome,cpf,senha,apto)