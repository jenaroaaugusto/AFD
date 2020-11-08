

caminho={   "q0":{"J":"q1"},
            "q1":{"1":"q2"},
            "q2":{"2":"q5","E":"q3","0":"q4"},
            "q3":{"N":"q2"},
            "q4":{"9":'q2'},             
        }
def possivel(palavra):
    print(f"Palavras {palavra}")
    chaves=["J","1","E","N","0","9","2"]
    if palavra in chaves:
        return True
    else: 
        return False
def arquivo(name): 
    flag="arquivo"
    x=[]

    lista = [line.strip() for line in open('upload/'+name)]
    for i in lista:
        resposta,status,transicoes=Verifica(i)
        print(f'Resposta:{resposta}, Status:{status}')
        x.append({"Palavra":resposta, "Status":status})
    # zip
    # x = zip(resposta, status)
   
    return x,"arquivo"

def Verifica(palavra):
    transicoes = []
    inicial="q0"
    final="q5"
    for i in palavra:
        proximo=caminho[inicial]
        print(possivel(i))
        if possivel(i) is False:
            print("Não aceita")
            return palavra,"OFF",transicoes
        print("Proximo:",proximo)
        print(f'Letra: {i}')
        transicoes.append({"proximo":proximo, "letra":i})
        
        inicial=proximo.get(i,[]) 
        if inicial==[]:
            # Não Aceito,
            mensagem=f"A palavra: {palavra} Não Aceito"
           
            print(mensagem)
            status="q6"
            return mensagem,status,transicoes
    
    if inicial == final:
        print("Aceito")
        status="ok"
        return palavra,status,transicoes
    else: 
        msg=f"A palavra: {palavra} não atingio o estado final estado atual: {inicial}"
        print(msg)
        status="q7"
        return msg,status,transicoes
        # status.split(" ")
# palavra="J12"
# msg,status=Verifica(palavra)

# print(msg,status)