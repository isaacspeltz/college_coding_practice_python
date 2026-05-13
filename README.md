# 🐍 Exercícios de Python — 1º Período · Ciência da Computação

Repositório com os exercícios práticos desenvolvidos ao longo do primeiro período do curso de Ciência da Computação. Os arquivos cobrem os fundamentos da programação em Python, desde estruturas de repetição até manipulação de listas e vetores.

---

## 📁 Estrutura do Repositório

```
array_exercises/
├── exercicios_for.py
├── exercicios_while.py
├── exercicios06_lista_vetores.py
└── exercicios07_listas.py
```

---

## 📄 Descrição dos Arquivos

### `exercicios_for.py` — Laço `for`

Exercícios focados no uso do laço `for` em conjunto com validação de entrada e construção de expressões matemáticas.

**Destaques:**
- Filtragem de números divisíveis por 3 mas não por 5, no intervalo de 1 a 100
- Validação de entrada com `while` para garantir número inteiro positivo
- Geração dinâmica da expressão de somatório `1 + 2 + 3 + ... + n = resultado`, com saída formatada

---

### `exercicios_while.py` — Laço `while`

Série de exercícios introdutórios e progressivos com o laço `while`, abordando contagem, validação e interação com o usuário.

**Exercícios incluídos:**
| # | Descrição |
|---|-----------|
| 1 | Contar de 1 a 10 |
| 2 | Contagem regressiva de 10 a 1 |
| 3 | Tabuada de um número entre 1 e 10, com validação |
| 4 | Leitura de palavra com validação de tamanho (3 a 10 letras) |
| 5 | Leitura de nota com validação de intervalo (0 a 10) |
| 6 | Cálculo do somatório de 1 até n |

---

### `exercicios06_lista_vetores.py` — Listas como Vetores

Exercícios que trabalham com listas Python no estilo de vetores de tamanho fixo, usando índices explícitos — uma abordagem próxima da programação estruturada clássica.

**Exercícios incluídos:**
| # | Descrição |
|---|-----------|
| 1 | Manipulação direta de um vetor pré-definido (soma, alteração de elemento, impressão) |
| 2 | Leitura de 6 valores inteiros e exibição do vetor |
| 3 | Leitura de 10 números reais e exibição dos seus quadrados |
| 4 | Soma de dois elementos do vetor em posições escolhidas pelo usuário |
| 5 | Contagem de valores pares em um vetor de 10 elementos |
| 6 | Identificação do maior e menor valor em um vetor de 10 elementos |
| 7 | Maior elemento e sua posição em um vetor de 10 elementos |
| 8 | Cálculo da média de 15 notas armazenadas em vetor |
| 9 | Contagem de negativos e soma dos positivos em um vetor |
| 10 | Maior, menor e média de 5 valores lidos |
| 11 | Maior e menor valores com suas respectivas posições |

> 💡 Este arquivo utiliza `import time` para adicionar um pequeno delay (`time.sleep`) na impressão de listas, tornando a saída mais legível no terminal.

---

### `exercicios07_listas.py` — Listas Dinâmicas

Exercícios com listas Python dinâmicas, aproveitando métodos nativos como `append`, `reverse`, `split`, `shuffle` e `index`.

**Exercícios incluídos:**
| # | Descrição |
|---|-----------|
| 1 | Geração de lista com 10 números aleatórios entre 1 e 100 |
| 2 | Leitura de 3 números e armazenamento em lista com `append` |
| 3 | Divisão de uma frase em lista de palavras com `split` |
| 4 | Inversão de uma lista com `reverse` |
| 5 | Encontrar a palavra mais longa e mais curta de uma lista |
| 6 | Separação de pares e ímpares em listas distintas e concatenação |
| 7 | Geração de lista de 1 a 100 e impressão dos números pares |
| 8 | Lista com os quadrados de 1 a 10 e soma total |
| 9 | Embaralhamento do alfabeto e desafio de adivinhar a posição de uma letra |
| 10 | Jogo da velha 3×3 funcional no terminal, com alternância de jogadores e detecção de vitória |

> 💡 Este arquivo utiliza `import random` para geração de números aleatórios e embaralhamento, e `import time` para efeitos de delay na saída.

---

## 🧠 Conceitos Abordados

- **Estruturas de repetição:** `for`, `while`, `break`, `continue`
- **Entrada e validação de dados:** `input()`, tratamento de valores inválidos
- **Operadores:** aritméticos, relacionais, lógicos e de módulo (`%`)
- **Listas como vetores:** acesso por índice, tamanho fixo
- **Listas dinâmicas:** `append`, `reverse`, `split`, `shuffle`, `index`
- **Strings:** manipulação, `len()`, `isalpha()`, `lower()`
- **Módulos padrão:** `random`, `time`
- **Lógica de jogos:** tabuleiro 2D, alternância de turno, condição de vitória

---

## 🚀 Como Executar

Certifique-se de ter o Python 3 instalado.

```bash
# Exemplo para rodar qualquer arquivo
python exercicios07_listas.py
```

Verifique a versão instalada:

```bash
python --version
```

---

## 👨‍🎓 Sobre

Exercícios desenvolvidos durante o **1º período do curso de Ciência da Computação**, como parte do aprendizado dos fundamentos de programação com Python.
