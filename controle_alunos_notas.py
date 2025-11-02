alunos_dicio = {
    "Ana": (8.0, 7.5, 9.0),
    "Carlos": (6.0, 5.0, 7.0)
}

alunos_set = {'Ana', 'Carlos'}

def cadastrar_aluno():
    '''Adiciona um aluno como chave em alunos_dicio e uma tupla vazia como valor'''

    aluno = input('Digite o nome do aluno que dejesa cadastrar: ').capitalize()
    #verifica alunos únicos a partir de um conjunto
    if aluno not in alunos_set:
        alunos_dicio[aluno] = ()
        alunos_set.add(aluno)
        print('-------------------------------------')
        print('Aluno(a) registrado com sucesso!')
    else:
        print('-------------------------------------')
        print('Aluno(a) já matriculado!')

def registrar_notas():
    '''Verifica se aluno já possui notas registradas, caso não, adiciona 3 notas em uma tupla como valor para chave aluno'''
    
    aluno = input('Digite o nome do aluno que deseja registrar as notas: ').capitalize()
    for k,v in alunos_dicio.items():
        if aluno == k and len(v) != 0:
            print('-------------------------------------')
            print(f'{aluno} já possui notas registradas')
            return
        
        #se o input corresponder a um aluno registrado e a tupla de suas notas estiver vazia
        elif aluno == k and len(v) == 0:
            notas = []
            try:
                #adiciona 3 notas a uma lista e depois da iteração converte a lista para uma tupla
                for i in range(1,4):
                    nota = float(input(f'Digite a nota {i}: '))
                    if nota >= 0 and nota <= 10:
                        notas.append(nota)
                    else:
                        print('Nota inválida. Notas devem estar entre 0 e 10! Tente novamente.')
                        return
                        
                alunos_dicio[aluno] = tuple(notas)
                print('-------------------------------------')
                print('Notas adicionadas com sucesso!')
            except ValueError:
                print('-------------------------------------')
                print('Nota apresenta valor inválido.')

            return
    print('-------------------------------------')
    print(f'Aluno(a) {aluno} não está matriculado.')

def listar_alunos_e_medias():
    '''Lista alunos de alunos_dicio e calcula suas repectivas médias a partir do valor de suas notas'''

    print('-------------------------------------')    
    for k,v in alunos_dicio.items():
        media = round(sum(v)/3,1) if len(v) != 0 else 'Notas não registradas'
        print(f'Aluno(a) : {k} - Média : {media}')

def buscar_aluno():
    '''Apresenta os dados do aluno inserido caso esteja em alunos_dicio'''

    aluno = input('Digite o nome do aluno que deseja buscar: ').capitalize()
    for k,v in alunos_dicio.items():
        if aluno == k:
            print('-------------------------------------')
            print(f'Aluno(a) matriculado. \nAluno(a) : {k} -  Notas : {v}')
            return
    print('-------------------------------------')
    print(f'Aluno(a) {aluno} não matriculado.')

def mostrar_aprovados_reprovados():
    '''Calcula a média de cada aluno e apartir disso define o status do aluno'''
    print('-------------------------------------')
    for k,v in alunos_dicio.items():
        media = round(sum(v)/3, 1)
        #se a tupla das notas não tiver itens, o status vai mostrar que as notas não foram registradas
        if len(v) == 0 :
            status = 'Notas não registradas' 
        elif media >= 7:
            status = 'Aprovado'
        else:
            status = 'Reprovado'

        print(f'{k} : {status}')

def relatorios():
    '''Apresenta o relatório desejado de acordo com o tipo de relatório escolhido.'''
    print('Tipos de relatório:\n1- Alunos cadastrados\n2- Médias individuais\n3- Status dos alunos')
    tipo_relatorio = input('Escolha o tipo de relatório : ')
    if tipo_relatorio == '1':
        print('-------------------------------------')
        print('Alunos cadastrados: ')
        print('-------------------------------------')
        for k in alunos_dicio.keys():
            print(k)

    elif tipo_relatorio == '2':
        print('-------------------------------------')
        print('Médias individuais: ')
        listar_alunos_e_medias()
        
    elif tipo_relatorio == '3':
        print('-------------------------------------')
        print('Status dos alunos: ')
        mostrar_aprovados_reprovados()
    else:
        print("Tipo Invalido! Não temos essa opção em nosso sistema!")
    


while True:
    print('-------------------------------------')
    print("1 - Cadastrar aluno")
    print("2 - Registrar notas")
    print("3 - Listar alunos e médias")
    print("4 - Buscar aluno")
    print("5 - Mostrar aprovados e reprovados")
    print("6 - Relatórios")
    print("0 - Sair")
    print('-------------------------------------')
    opcao = input("Escolha uma opção: ")
    print('-------------------------------------')

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        registrar_notas()
    elif opcao == "3":
        listar_alunos_e_medias()
    elif opcao == "4":
        buscar_aluno()
    elif opcao == "5":
        mostrar_aprovados_reprovados()
    elif opcao == "6":
        relatorios()
    elif opcao == "0":
        print("Fim do sistema!")
        break
    else:
        print("Opção inválida! Não temos essa opção em nosso sistema!")