# mini-projeto-python-EmillyBarbosa-LetíciaLeandro


# 🛒**Sistema de Controle de Produtos**

Um sistema simples e interativo no terminal que simula o controle de estoque de uma pequena loja e que permite cadastrar, listar, buscar, atualizar e excluir produtos.

<hr>
## ⚙️ **Funcionalidades do Sistema**

- **Menu principal:** O sistema mostra um menu com 6 opções.

- **Cadastrar produto (1):** O sistema pede código (único), nome, preço e quantidade em estoque, guarda os valores em um dicionário e adiciona a lista `produtos`.

- **Listar produtos (2):** Mostrar a lista completa dos produtos armazenados no sistema.

- **Buscar produto (3):** Sistema busca produto a partir do código inserido e exibe as informações do produto encontrado.

- **Atualizar produto (4):**  O usuário informa o código do produto que deseja atualizar e o sistema atualiza as informações do produto (código, nome, preço, quantidade).

- **Excluir Produto (5):** O usuário informa o código do produto que deseja excluir e o sistema localiza o produto desejado e o remove da lista `produtos`.

- **Sair (0):** Fecha o programa.


<hr>

## 💡 **Funcionamento Geral**


- Os produtos são armazenados a partir de uma lista (`produtos`) que contem dicionários (cada dicionário representa um único produto).
- O conjunto `codigos_set`  auxilia na prevenção de duplicadas para os produtos já cadastrados.
- O programa é rodado é um while loop, que apresenta 6 opções numeradas, e permite interações contínuas até o usuário decidir finalizar.


<hr>

## 📋**Exemplo do Menu**

```
-------------------------------
1 - Cadastrar o produto
2 - Listar os produtos
3 - Buscar o produto
4 - Atualizar o produto
5 - Excluir o produto
0 - Sair
-------------------------------
Escolha uma opção:

```


<hr>

## 💻**Exemplos de Uso**

Exemplo 1: Cadastrar produto.  

```
-------------------------------
Escolha uma opção: 1
-------------------------------
Digite o código do produto: 104
Digite o nome do produto: Leite
Digite o preço do produto: 5.2
Digite a quantidade do produto: 12
-------------------------------
Produto cadastrado com sucesso!
-------------------------------

```

Exemplo 2: Atualizar produto.

```
-------------------------------
Escolha uma opção: 4
-------------------------------
Digite o código do produto que dejesa atualizar: 104
Qual opção deseja atualizar (codigo, nome, preço, quantidade) : quantidade
quantidade atual : 12
Dejesa atualizar para qual valor? 25
-------------------------------
Atualização feita com sucesso!
-------------------------------
```



<hr>

<hr>
<hr>

<hr>


# 📝**Sistema de Controle de Notas e Alunos**

Um sistema simples e interativo no terminal que tem como objetivo ajudar o professor de uma escola a consultar rapidamente o desempenho da
turma. No sistema é possível cadastrar alunos, registrar notas, listar alunos e médias, buscar aluno, mostrar aprovados e reprovados e gerar relatórios.


<hr>

## ⚙️ **Funcionalidades do Sistema**

- **Menu principal**: O sistema mostra um menu com 7 opções.

- **Cadastrar aluno(1):** Adicionar um novo aluno e verificar se está registrado no sistema.
    
- **Registrar notas(2):** Adiciona três notas por aluno, podendo registrar notas que estão entre 0 a 10.
    
- **Listar alunos e médias(3):** Mostra os alunos cadastrados junto com suas respectivas médias.
    
- **Buscar aluno(4):** Busca aluno a partir do nome e mostra seus dados (Nome e notas).
    
- **Mostrar aprovados e reprovados(5):** Exibe os status dos alunos (Aprovado/ Reprovado) com base nas suas respectivas médias.
    
- **Relatórios(6):** Oferece três tipos de relatórios automáticos:
    
    1. Lista de alunos cadastrados
        
    2. Médias individuais
        
    3. Status (aprovados ou reprovados)
        
- **Sair(0):** Fecha o programa.


<hr>

## 💡 **Funcionamento Geral**

- Nomes dos alunos são armazenados como chaves em um dicionário chamado `alunos_dicio`.
- O valor de cada chave aluno é uma **tupla** que armazena suas três notas.
- O **conjunto** `alunos_set` auxilia na prevenção de duplicadas para os alunos matriculados.
- O programa é rodado é um while loop, que apresenta 7 opções numeradas, e permite interações contínuas até o usuário decidir finalizar.


<hr>

## 📋**Exemplo do Menu**

```
-------------------------------------
1 - Cadastrar aluno
2 - Registrar notas
3 - Listar alunos e médias
4 - Buscar aluno
5 - Mostrar aprovados e reprovados
6 - Relatórios
0 - Sair
-------------------------------------
Escolha uma opção:

```


<hr>

## 💻**Exemplos de Uso**

Exemplo 1: Registrar Notas.

```
-------------------------------------
Escolha uma opção: 2
-------------------------------------
Digite o nome do aluno que deseja registrar as notas: Caio
Digite a nota 1: 4
Digite a nota 2: 7.5
Digite a nota 3: 10
-------------------------------------
Notas adicionadas com sucesso!
-------------------------------------
```

Exemplo 2: Exibir relatório - Status dos Alunos.

```
-------------------------------------
Escolha uma opção: 6
-------------------------------------
Tipos de relatório:
1- Alunos cadastrados
2- Médias individuais
3- Status dos alunos
Escolha o tipo de relatório : 3
-------------------------------------
Status dos alunos: 
-------------------------------------
Ana : Aprovado
Carlos : Reprovado
Caio : Aprovado
-------------------------------------
```


<hr>
<hr>


## 👥 Contribuidores 

| Nome            | GitHub                         |
| --------------- | ------------------------------ |
| Emilly Barbosa  | https://github.com/emi-gby     |
| Letícia Leandro | https://github.com/MusMus19Leh |

 
