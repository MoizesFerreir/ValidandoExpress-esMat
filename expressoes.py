expre = str(input('Digite uma expressão: '))
pilha = []
for sim in expre:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('É uma expressão valida')
else:
    print('Não é um expressão valida')
