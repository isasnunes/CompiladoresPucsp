"""
Disciplina: Compiladores - PUC-SP
Scanner léxico para tokenizar texto em português.

Autores: 
Isabela Nunes 
Pedro Huck
Sthefany Viveiros
"""

import re
import sys

def tokenizar(texto):
    """
    Quebra o texto em tokens usando expressões regulares.
    Tokens reconhecidos:
    - Palavras com acentos
    - Palavras com hífen
    - Números
    - Pontuação

    Parâmetro:
        texto (str): string contendo todo o conteúdo do arquivo de entrada.

    Retorno:
        list: lista contendo todos os tokens encontrados no texto.
    """

    regex = r"""
        \.\.\. |                    # reticências
        \d+(?:[.,]\d+)? |          # números
        [A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)* |  # palavras
        [.,!?;:"()\[\]—-]          # pontuação
    """

    tokens = re.findall(regex, texto, re.VERBOSE)
    return tokens



def main():
    """
    Função principal:
    - Recebe arquivo de entrada por argumento
    - Gera tokens
    - Salva no output.txt
    """

    #Verifica se o usuário informou o arquivo de entrada
    #sys.argv contém os argumentos passados na execução do programa
    if len(sys.argv) < 2:
        print("Uso: python scanner.py <arquivo.txt>")
        return

    
    arquivo_entrada = sys.argv[1]    #Nome do arquivo de entrada recebido pela linha de comando
    arquivo_saida = "output.txt"    #Nome do arquivo onde os tokens serão salvos

    try:
        #Abre o arquivo de entrada em modo leitura
        #encoding UTF-8 garante suporte a caracteres acentuados
        with open(arquivo_entrada, "r", encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        #Tratamento caso o arquivo não exista
        print("Erro: arquivo de entrada não encontrado.")
        return

    tokens = tokenizar(texto)    #Chama a função que realiza a tokenização do texto

    print("Primeiros 50 tokens:")
    print(tokens[:50])    #Mostra no terminal apenas os primeiros 50 tokens

    with open(arquivo_saida, "w", encoding="utf-8") as out:    #Abre o arquivo de saída para escrita
        for token in tokens:
            out.write(token + "\n")    #Cada token será salvo em uma linha

    #informações finais para o usuário
    print(f"\nTotal de tokens: {len(tokens)}")
    print("Tokens salvos em output.txt")


if __name__ == "__main__":
    main()
