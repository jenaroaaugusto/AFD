palavra="J1N"
caminho={   "q0":{"J":"q1"},
            "q1":{"1":"q2"},
            "q2":{"2":"q5","E":"q3","0":"q4"},
            "q3":{"N":"q2"},
            "q4":{"9":'q2'}

        }
inicial="q0"
final="q5"
for i in palavra:
    proximo=caminho[inicial]
    print("Proximo:",proximo)
    print(f'Letra: {i}')
    inicial=proximo.get(i,[])
    
    if not inicial:
        
        print(f"Estado: {i} Não atinge o estado final")
        exit()
        break
print(inicial,final)
if inicial == final:
    print("Aceito")
else: 
    # print ()
    print(inicial,"Não Aceito, Estado final não atingido")