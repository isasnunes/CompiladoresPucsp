#!/bin/bash

while true; do
    # Lê a linha recebida. O comando quebra o loop quando o arquivo acabar para não rodar ao infinito.
    if ! read -r linha; then
        break
    fi

    # O comando tr remove espaços (' '), tabs ('\t') e carriage returns ('\r')
    linha_limpa=$(echo "$linha" | tr -d ' \t\r')

    echo "[SCANNER] Linha recebida e limpa: '$linha_limpa'"
done