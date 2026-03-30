import re

def tokenize(texto):
    # Definindo as regras do Autômato Finito
    # O formato (?P<NOME>regex) cria um "grupo nomeado", facilitando a classificação
    regras = [
        ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identificadores (variáveis)
        ('NUM', r'\d+'),                    # Números inteiros
        ('OP', r'[=+\-*]'),                 # Operadores
        ('ESPACO', r'[ \t]+')               # Espaços e tabs (para ignorar depois)
    ]
    
    # Junta todas as regras com o operador OU (|)
    regex_mestra = '|'.join(f'(?P<{tipo}>{padrao})' for tipo, padrao in regras)
    
    lista_tokens = []
    
    # re.finditer percorre a string e acha todas as ocorrências da regex
    for match in re.finditer(regex_mestra, texto):
        tipo = match.lastgroup      # Pega o nome do grupo que deu "match" (ID, NUM, etc)
        lexema = match.group(tipo)  # Pega o texto exato que foi capturado
        
        # O scanner ignora espaços em branco, então só salvamos o resto
        if tipo != 'ESPACO':
            lista_tokens.append((tipo, lexema))
            
    return lista_tokens

# Testando com a string do livro do dragão
codigo = "position = initial + rate * 60"
resultado = tokenize(codigo)

print(resultado)