from Funcoes.lista_de_tarefas import listar_tarefas, desfazer, refazer


opcoes = [
        {'[1]': 'Adicionar tarefa'},
        {'[2]': 'Listar tarefas'},
        {'[3]': 'Desfazer a ultima tarefa'},
        {'[4]': 'Refazer a ultima tarefa'},
        {'[5]': 'Sair'}]
for opc in opcoes:
    for k, v in opc.items():
        print(f'{k} - {v}')
Lista = []
while True:
    usuario = input('Qual á sua opção: ').strip()

    if usuario in '1':
        while True:
            atividade = input('O que gostaria de adicionar a sua lista de afazeres ?').strip().capitalize()
            Lista.append(atividade)
            if atividade == 'Parar':
                Lista.pop()
                break

    if usuario in '2':
        if len(Lista) == 0:
            print('Sua lista esta vazia!')
        else:
            print('Aqui esta sua lista')
            listar_tarefas(Lista)

    if usuario in '3':
        des = desfazer(Lista)
        print(f'Foi removido {des} da sua lista!')
    if usuario in '4':
        ref = refazer(Lista, des)
        print(f'Foi add novamente {des} a lista!')

    if usuario in '5':
        print('Fim do programa')
        if len(Lista) != 0:
            print('Sua lista!')
            listar_tarefas(Lista)
        break
