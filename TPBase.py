
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
def Verifica(palavra):
    inicial="q0"
    final="q5"
    for i in palavra:
        proximo=caminho[inicial]
        print(possivel(i))
        if possivel(i) is False:
            print("Não aceita")
            return palavra,"OFF"
        print("Proximo:",proximo)
        print(f'Letra: {i}')
        inicial=proximo.get(i,[]) 
        if inicial==[]:
            # Não Aceito,
            mensagem=f"A palavra: {i} Não Aceito"
            # mensagem=f"A palavra: {i} Não atinge o estado final,Atinge o Estado: {inicial}"
            # print(f"A palavra: {i} Não atinge o estado final,Atinge o Estado: {inicial}")
            print(mensagem)
            status="q6"
            return mensagem,status
    
    if inicial == final:
        print("Aceito")
        status="ok"
        return "Aceito",status
    else: 
        msg=f"A palavra:{inicial} não atingio o estado final"
        print(msg)
        status="q7"
        return msg,status
        # status.split(" ")
# palavra="J12"
# msg,status=Verifica(palavra)

# print(msg,status)