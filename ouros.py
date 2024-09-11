# ira desenhar o naipe de ouros
# simbolo = muda a composição do desenho
# tamanho = metade do numero de linhas
def ouros(simbolo=' ', tamanho=11, simbolo_fundo=True):
    # NÃO É POSSÍVEL FAZER COM MAIS DE UM SIMBOLO
    if len(simbolo) > 1:
        # Pega o primeiro caracter
        simbolo = simbolo[0]
    # se par adiciona 1, por questão da formatação
    if tamanho % 2 == 0:
        tamanho += 1
    # Linha em cima *opcional
    print('\033[7;37m-' * (tamanho + 2) + '\033[m')
    # https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
    cor_fundo_simbolo = ('\033[33;41m')
    # altera a cor e retira a cor de fundo do simbolo
    if not simbolo_fundo:
        cor_fundo_simbolo = ('\033[31;47m')
    cor_fundo_carta = '\033[7;37;47m'
    cor_reset = '\033[m'
    # parte de cima, triangulo normal
    # faz um loop de um até o tamanho, sendo sempre ímpar
    for i in range(1, tamanho + 1, 2):
        # string variavel
        linha = simbolo * i # quantidade de simbolos na linha
        # linha antes e depois: para formatação (antes) e visual (antes e depois)
        linha_antes_depois = (
                       cor_fundo_carta  
                       + ' ' * ((tamanho - i) // 2 + 1) # metade do tamanho para servir como centralizador
                       + cor_reset
                       )
        # desenho parte de cima
        print(f'{ 
                 linha_antes_depois 
                 + cor_fundo_simbolo 
                 + linha 
                 + cor_reset 
                 + linha_antes_depois
                 }')
    # parte de baixo, triangulo invertido
    # faz loop em ordem decrescente a partir do 1° ímpar menor que o tamanho
    for i in range(tamanho - 2, 0, -2):
         # string variavel
        linha = simbolo * i
        # linha antes e depois: para formatação (antes) e visual (antes e depois)
        linha_antes_depois = (
                       cor_fundo_carta  
                       + ' ' * ((tamanho - i) // 2 + 1)
                       + cor_reset
                       )
        # desenho parte de baixo
        print(f'{ 
                 linha_antes_depois 
                 + cor_fundo_simbolo 
                 + linha 
                 + cor_reset 
                 + linha_antes_depois
                 }')
    # Linha de baixo *opcional
    print('\033[7;37m-' * (tamanho + 2) + '\033[m')


ouros()
ouros('*')
ouros('a', 20)
ouros('+', simbolo_fundo=False)