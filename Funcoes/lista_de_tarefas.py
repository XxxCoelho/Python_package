def listar_tarefas(lista):
    for i, tarefas in enumerate(lista, 1):
        print(f'{i}° - {tarefas}')


def desfazer(Lista):
    desfaz = Lista.pop(-1)
    return desfaz


def refazer(Lista, Ultimo_elemento):
    return Lista.append(Ultimo_elemento)
