
# Fução previa de palavra

def acabou(parametro):
    if parametro==0:
        print("Palavra Vazia não e aceita")
    if parametro==2:
        print("Palavra aceita no Foi para o Q6")
# def atualiza(dados,letra):


def automato(palavra):
    arquitetura={}
    
    print(palavra)

    if len(palavra)==0:
        acabou(0)
    for i in range(len(palavra)):

        if "J" == palavra[0]:
            print("ok")
            arquitetura={"J":palavra.index(i)}
            
        elif palavra.index("J")!=0:
            acabou(2) 

# Estrutura aceita J1(09+EN)*2

# if palavra[0]











palavra=input("Digite uma plavra:")

palavra=list(palavra.upper())

automato(palavra)
