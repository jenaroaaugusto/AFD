

with open("upload/uploaded_file.txt") as lines:
    lista1 = []
    for i in lines:
        lista1.append(i.strip())
        

lista = [line.strip() for line in open('upload/uploaded_file.txt')]

print(f"L compreenhension {lista} l1 {lista1}")