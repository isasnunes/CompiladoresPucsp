"""
Scanner léxico para tokenizar texto em português.


Autores: 
Isabela Nunes 
Pedro Huck
Sthefany Viveiros


Disciplina: Compiladores - PUC-SP
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
    - Salva no output.txt (já existente)
    """

    if len(sys.argv) < 2:
        print("Uso: python scanner.py <arquivo.txt>")
        return

    arquivo_entrada = sys.argv[1]
    arquivo_saida = "output.txt"  # já existe na pasta

    try:
        with open(arquivo_entrada, "r", encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        print("Erro: arquivo de entrada não encontrado.")
        return

    tokens = tokenizar(texto)

    # Mostra exemplo
    print("Primeiros 50 tokens:")
    print(tokens[:50])

    # Escreve no output.txt (um token por linha)
    with open(arquivo_saida, "w", encoding="utf-8") as out:
        for token in tokens:
            out.write(token + "\n")

    print(f"\nTotal de tokens: {len(tokens)}")
    print("Tokens salvos em output.txt")


if __name__ == "__main__":
    main()