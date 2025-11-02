

produtos = [{'codigo': 101, 'nome': 'Arroz', 'preço': 7.99, 'quantidade': 10},
            {'codigo': 102, 'nome': 'Refrigerante', 'preço': 5.43, 'quantidade': 4},
            {'codigo': 103, 'nome': 'Laranja', 'preço': 1.23, 'quantidade': 42}]

codigos_set = set([item['codigo'] for item in produtos])

categorias_disponiveis = ('Alimentos', 'Bebidas')

def cadastrar_produto():
    '''Verifica produtos únicos, armazena produto em um dicionário e adiciona produto na lista de produtos.'''
    try:
        codigo = int(input('Digite o código do produto: '))
        if codigo in codigos_set:
            print('-------------------------------')
            print('Código já utilizado. Tente novamente.')
            return

        nome = input('Digite o nome do produto: ').capitalize()
        preco = float(input('Digite o preço do produto: '))
        quant = int(input('Digite a quantidade do produto: '))
        
        codigos_set.add(codigo)

        #adiciona items no dicionário
        produto_dict = {}
        produto_dict['codigo'] = codigo
        produto_dict['nome'] = nome
        produto_dict['preço'] = preco
        produto_dict['quantidade'] = quant

        #adiciona dicionário na lista
        produtos.append(produto_dict)

        print('-------------------------------')
        print('Produto cadastrado com sucesso!')
    
    #verifica tipo de dado
    except ValueError:
        print('-------------------------------')
        print('Valor inserido não condiz com o tipo de dado utilizado!')

def listar_produtos():
    '''Lista todos os produtos em formato de dicionário.'''
    for i in produtos:
        print(i)

def buscar_produto():
    '''Define o codigo do produto e printa seus atributos se o valor inserido condizer com os valores dos produtos'''

    try:
        codigo = int(input('Digite o código do produto: '))
        #itera sobre a lista de produtos e procura em cada dicionario se o valor inserido corresponde ao valor da chave do dicionario
        for dicio in produtos:
            if dicio['codigo'] == codigo:
                print('-------------------------------')
                print('Produto encontrado. \nInformações sobre: ')
                for k,v in dicio.items():
                    print(f'{k} : {v}')
                return
            
        print('-------------------------------')    
        print('Produto não encontrado.')

    except ValueError:
        print('-------------------------------')
        print('Valor inserido não condiz com o tipo de dado utilizado!')



def atualizar_produto():
    '''Atualiza os atributos do produto de acordo com a opção inserida'''
    try:
        codigo = int(input(f'Digite o código do produto que dejesa atualizar: '))
        #verifica se existe um codigo nos produtos que corresponde ao codigo inserido.
        for dicio in produtos:
            if dicio['codigo'] == codigo:
                opcao_atualizar = input('Qual opção deseja atualizar (codigo, nome, preço, quantidade) : ').lower()
                #dispoe o valor atual da opção escolhida, verifica repetidos para a opção 'código' e atualiza o valor da informação escolhida pelo usuário
                if opcao_atualizar == 'codigo' or opcao_atualizar == 'código':
                    print(f'Código atual : {dicio['codigo']}')
                    verificar_atualizacao(dicio)
                    return
                
                elif opcao_atualizar == 'nome':
                    print(f'Nome atual : {dicio['nome']}')
                    atualizacao = input('Dejesa atualizar para qual valor? ').capitalize()
                    dicio['nome'] = atualizacao

                    print('-------------------------------')    
                    print('Atualização feita com sucesso!')
                    return
                    

                elif opcao_atualizar == 'preço' or opcao_atualizar == 'preco':
                    print(f'Preço atual : {dicio['preço']}')
                    try: 
                        #atualiza o valor caso o tipo de dado esteja correto
                        atualizacao = float(input('Dejesa atualizar para qual valor? '))
                        dicio['preço'] = atualizacao

                        print('-------------------------------')    
                        print('Atualização feita com sucesso!')
                    
                    except ValueError:
                        print('-------------------------------') 
                        print('Valor inserido não condiz com o tipo de dado utilizado!')

                    return
                
                elif opcao_atualizar =='quantidade':
                    print(f'Quantidade atual : {dicio['quantidade']}')
                    try: 
                        #atualiza o valor caso o tipo de dado esteja correto
                        atualizacao = int(input('Dejesa atualizar para qual valor? '))
                        dicio['quantidade'] = atualizacao

                        print('-------------------------------')    
                        print('Atualização feita com sucesso!')
                    
                    except ValueError:
                        print('-------------------------------') 
                        print('Valor inserido não condiz com o tipo de dado utilizado!')

                    return

                else:
                    print('-------------------------------')    
                    print('Não temos essa opção no sistema!')
                    return

        print('-------------------------------')
        print('Código do produto não encontrado.')

    except ValueError:
        print('-------------------------------')
        print('Valor inserido não condiz com o tipo de dado utilizado!')

def verificar_atualizacao(dicio):
    '''Verifica items únicos para código, caso houver repetidos o item não é atualizado'''

    try:
        atualizacao = int(input('Dejesa atualizar para qual valor? '))
        if atualizacao in codigos_set:
            print('-------------------------------')  
            print('Código já utilizado. Tente novamente.')
            return
        elif atualizacao not in codigos_set:
            dicio[opcao] = atualizacao


    except ValueError:
        print('-------------------------------') 
        print('Valor inserido não condiz com o tipo de dado utilizado!')
        return

    print('-------------------------------')    
    print('Atualização feita com sucesso!')
        

def excluir_produto():
    '''Remove o produto da lista de produtos a partir do código inserido'''
    try:
        codigo = int(input('Digite o código do produto que dejesa excluir: '))
        for dicio in produtos:
            #remove o produto do dicionário se tiver o código correspondente em um dicionário na iteração
            if dicio['codigo'] == codigo:
                produtos.remove(dicio)
                print('-------------------------------')
                print('Produto removido com sucesso!')
                return
            
            print('-------------------------------')
            print('Código do produto não encontrado.')

    except ValueError:
        print('-------------------------------')
        print('Valor inserido não condiz com o tipo de dado utilizado!')


while True:
    print('-------------------------------')
    print('1- Cadrastar o produto')
    print('2- Listar os produtos')
    print('3- Buscar o produto')
    print('4- Atualizar o produto')
    print('5- Excluir o produto')
    print('0- Sair')
    print('-------------------------------')

    opcao = input('Escolha uma opção: ')

    print('-------------------------------')

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        buscar_produto()
    elif opcao == '4':
        atualizar_produto()
    elif opcao == '5':
        excluir_produto()
    elif opcao == '0':
        print('Sistema finalizado!')
        break
    else:
        print('Não existe essa opção em nosso sistema! Escolha outra:')