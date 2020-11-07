ok

caminho={   "q0":{"J":"q1","E":"q6","0":"q6","2":"q6","N":"q6","9":"q6", "1":"q6"},
            "q1":{"1":"q2","E":"q6","0":"q6","2":"q6","N":"q6","J":"q6", "9":"q6"},
            "q2":{"2":"q5","E":"q3","0":"q4", "N":"q6","J":"q6","9":"q6","1":"q6",},
            "q3":{"N":"q2","E":"q6","0":"q6","2":"q6","9":"q6","1":"q6"},
            "q4":{"9":'q2',"1":"q6","J":"q6","N":"q6","2":"q6","0":"q6","E":"q6"},             
        }


        caminho={   "q0":{"J":"q1","E":"q6","0":"q6","2":"q6","N":"q6","9":"q6", "1":"q6"},
            "q1":{"1":"q2","E":"q6","0":"q6","2":"q6","N":"q6","J":"q6", "9":"q6"},
            "q2":{"2":"q5","E":"q3","0":"q4", "N":"q6","J":"q6","9":"q6","1":"q6",},
            "q3":{"N":"q2","E":"q6","0":"q6","2":"q6","9":"q6","1":"q6"},
            "q4":{"9":'q2',"1":"q6","J":"q6","N":"q6","2":"q6","0":"q6","E":"q6"},             
        }

def Verifica(palavra):
    inicial="q0"
    final="q5"
    for i in palavra:
        proximo=caminho[inicial]
        print("Proximo:",proximo)
        print(f'Letra: {i}')
        inicial=proximo.get(i,[]) 
        if not inicial:
            mensagem=f"A palavra: {i} Não atinge o estado final,Atinge o Estado: {inicial}"
            # print(f"A palavra: {i} Não atinge o estado final,Atinge o Estado: {inicial}")
            print(mensagem)
            status="q6"
            return mensagem,status
        elif inicial =="q6":
            mensagem=f"A palavra: {i} Não atinge o estado final, atinge o {inicial}"
            # print(f"A palavra: {i} Não atinge o estado final, atinge o {inicial}")
            print(mensagem)
            status="q6"
            return mensagem,status
        elif inicial == []:
                msg=f"{inicial},Não Aceito, Estado final não atingido"
                status="q7"
                print(msg)
    if inicial == final:
        print("Aceito")
        return "q5"
    else: 
        msg=f"{inicial},Não Aceito, Estado final não atingido"
        status="q7"
        print(msg)
        
        return msg,status



        # palavra="J12"
caminho={   "q0":{"J":"q1","E":"q6","0":"q6","2":"q6","N":"q6","9":"q6", "1":"q6"},
            "q1":{"1":"q2","E":"q6","0":"q6","2":"q6","N":"q6","J":"q6", "9":"q6"},
            "q2":{"2":"q5","E":"q3","0":"q4", "N":"q6","J":"q6","9":"q6","1":"q6",},
            "q3":{"N":"q2","E":"q6","0":"q6","2":"q6","9":"q6","1":"q6"},
            "q4":{"9":'q2',"1":"q6","J":"q6","N":"q6","2":"q6","0":"q6","E":"q6"},             
        }

def Verifica(palavra):
    inicial="q0"
    final="q5"
    for i in palavra:
        proximo=caminho[inicial]
        print("Proximo:",proximo)
        print(f'Letra: {i}')
        inicial=proximo.get(i,[]) 
        if not inicial:
            print('No primeir0')
            mensagem=f"A palavra: {i} Não atinge o estado final,Atinge o Estado: {inicial}"
            # print(f"A palavra: {i} Não atinge o estado final,Atinge o Estado: {inicial}")
            print(mensagem)
            status="q6"
            return mensagem,status
        elif inicial =="q6":
            print('No segundo0')
            mensagem=f"A palavra: {i} Não atinge o estado final, atinge o {inicial}"
            # print(f"A palavra: {i} Não atinge o estado final, atinge o {inicial}")
            print(mensagem)
            status="q6"
            return mensagem,status
        elif inicial== []:
            msg=f"{inicial},Não Aceito, Estado final não atingido"
            status="q7"
            print(msg)



    if inicial == final:
        print("Aceito")
        return "q5"
    else: 
        msg=f"{inicial},Não Aceito, Estado final não atingido"
        status="q7"
        print(msg)
        
        return msg,status