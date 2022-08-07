#Valor embaralhado solicitado do usuário

def Espelho(dig):
    return dig[::-1]
espelhando = input("Digite uma palavra para espelhamento: ")

print(f'Este é o valor espelhado: {Espelho(espelhando)}')
