def validar_parenteses(expressao):
    pilha = []
    
    for caractere in expressao:
        if caractere == '(':
            pilha.append('(')  # Guarda o parêntese aberto
        elif caractere == ')':
            if len(pilha) > 0:
                pilha.pop()  # Encontrou o par par, remove da pilha
            else:
                return False  # Fechou um parêntese sem nenhum ter sido aberto
                
    return len(pilha) == 0  # Se a pilha terminar vazia, está correto

# Interação com o usuário
usuario_expr = input("Digite uma expressão matemática com parênteses: ")

if validar_parenteses(usuario_expr):
    print("Sua expressão está correta!")
else:
    print("Sua expressão está errada! Verifique os parênteses.")