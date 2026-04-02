# CompiladoresPucsp

Atividade 1:

<img width="701" height="186" alt="image" src="https://github.com/user-attachments/assets/6e037d7c-327c-440b-a7a1-ca101c2185df" />

Atividade 2:

<img width="652" height="211" alt="image" src="https://github.com/user-attachments/assets/d82a8f22-9ad6-4bf9-9fce-7759fec60428" />

A expressão regular construída combina três padrões através do operador lógico OU (|). O primeiro bloco [a-zA-Z_][a-zA-Z0-9 ]* identifica as variáveis, o segundo \d+ captura os valores numéricos inteiros, e o terceiro [=+\-*] reconhece os operadores matemáticos e de atribuição. Com isso, a regex atua como um analisador léxico, extraindo sequencialmente os tokens válidos da string e ignorando os espaços em branco.

2.1 Extra (e-mail):

<img width="635" height="147" alt="image" src="https://github.com/user-attachments/assets/47b0ac64-ad6f-4607-9af9-cb730d664d76" />

A expressão é dividida em blocos lógicos para validar a estrutura padrão de um endereço de e-mail, o padrão [\w.-]+ inicial captura o nome do usuário, permitindo letras, números, sublinhados (\w), pontos e hifens. Em seguida, o símbolo @ é validado literalmente, o segundo [\w.-]+ captura o domínio da mesma forma (ex: gmail, pucsp) e, por fim, \.[a-zA-Z]{2,} exige um ponto literal seguido de, no mínimo, duas letras para validar a extensão final (como .com ou .br).

Atividade 3:

Removendo //

<img width="630" height="219" alt="image" src="https://github.com/user-attachments/assets/5f3ce9ed-4365-4aea-9d5b-f378004c7a5c" />
<img width="613" height="215" alt="image" src="https://github.com/user-attachments/assets/9174bb12-b9d8-409f-a90f-3ff717daf4eb" />

Removendo /* */

<img width="645" height="231" alt="image" src="https://github.com/user-attachments/assets/d134e7ef-66a2-4a65-90d3-040c7901632f" />
<img width="617" height="216" alt="image" src="https://github.com/user-attachments/assets/81047300-a0f4-4398-b1e4-30c5c9751b20" />

Subistituindo =

<img width="598" height="234" alt="image" src="https://github.com/user-attachments/assets/e9686a61-ceb9-42da-9450-43e642c786b8" />
<img width="607" height="206" alt="image" src="https://github.com/user-attachments/assets/c03230e1-087f-43d2-b216-4363f35795a0" />

CSV
Trocar Português para Inglês

<img width="616" height="245" alt="image" src="https://github.com/user-attachments/assets/68db5aca-3fc6-4002-9c4b-ab1e791461d6" />
<img width="619" height="290" alt="image" src="https://github.com/user-attachments/assets/8a4a88e8-de51-4a57-b3bc-2945b99ced79" />
<img width="598" height="284" alt="image" src="https://github.com/user-attachments/assets/78ad7e6b-51a1-4db8-a1f3-cc236e5aa839" />

CSv em TSV

<img width="597" height="262" alt="image" src="https://github.com/user-attachments/assets/e84f59b3-bb16-4306-b465-4b5e08f23aa9" />
<img width="613" height="276" alt="image" src="https://github.com/user-attachments/assets/a0d9bf7b-8310-44ab-b626-f744c83851ed" />

Atividade 4:

<img width="1000" height="141" alt="image" src="https://github.com/user-attachments/assets/29c6361e-330e-41cb-90e2-cc78111094f7" />

Atividade 5:
  DFA para reconhecer números inteiros:
<img width="1028" height="970" alt="image" src="https://github.com/user-attachments/assets/e364c460-6c62-40fb-9f4c-8bfc8047f2d6" />

  DFA para identificadores:
<img width="1078" height="1001" alt="image" src="https://github.com/user-attachments/assets/cd8c7d2c-bbb2-44bc-9979-a5b3611e5002" />

  NFA para operador = e ==:
<img width="1211" height="938" alt="image" src="https://github.com/user-attachments/assets/e45416ba-c9ad-472d-8f3d-b82598254a2c" />


Atividade 6: O tokenizer da openIA separa position em pos + ition por utilziar o metodo BPE, diferente dos analizadores léxicos, o BPE foca em criar tokens apartir de reconhecimento de padrões e não pela singificancia da palavra
