"""
Exercício: undo e redo.................................................................

Faça uma lista de 'tarefas' com as seguintes opções:
    # adicionar tarefa
    # listar tarefas
    # opção de desfazer tarefa (a cada vez que chamarmos, desfaz a última ação) - undo
    # opção de refazer  tarefa (a cada vez que chamarmos, refaz a útima ação  ) - redo

    Ex:

    ['t1', 't2', 't3', ] --> escolho a opcao 'desfazer', fica -->  ['t1', 't2'] 
    --> escolho a opcao 'refazer', fica: ['t1', 't2', 't3']

......................................................................................

"""

# Função: responsável por exibir menu de opções.
def menu():
    print('\n[ a  ] adicionar tarefa\n'
          '[ ls ] listar tarefas  \n'
          '[ d  ] desfazer tarefa \n'
          '[ r  ] refazer tarefa  \n'
          '[ s  ] sair            \n')


# Função: adiciona tarefas digitadas pelo usuário.
def add(tarefa, lista_tarefas, lista_copia, tarefas_removidas):
    lista_tarefas.append(tarefa)
    copiar(lista_tarefas, lista_copia)
    
    lista_copia.extend(tarefas_removidas) 

  
# Função: lista as 'tarefas' cadastradas.
def listar(lista_tarefas):
    print(f'\nTarefa(s): {lista_tarefas}')


# Função: realiza a cópia da lista de tarefas.
def copiar(lista_tarefas, lista_copia):
    lista_copia.clear()
    for i in lista_tarefas:
        lista_copia.append(i)

    
# Função: Undo - responsável por anular uma determinada ação.
def desfazer(lista_tarefas, tarefas_removidas):
    try:
        removido = lista_tarefas.pop()
        tarefas_removidas.insert(0,removido)
        listar(lista_tarefas)
    except IndexError:
        print('Sua lista de tarefas está vazia. Nada para desfazer !!')

  
# Função: Redo - responsável refazer uma determinada ação. 
def refazer(lista_tarefas, lista_copia):
    tamanho = len(lista_tarefas)
    if tamanho < len(lista_copia):
        lista_tarefas.append(lista_copia[tamanho])
        listar(lista_tarefas)
    else:
        print('Limite para refazer alcançado! Nada para refazer')


# Função principal.    
def main():

    # Dicionário de dados:
    lista_tarefas = []
    lista_copia = []
    tarefas_removidas = []
    
    while True:
        menu()
        op1 = input('--> Opção: ').lower()
        
        # Escolha de opções:
        if op1 == 's':
           op2 = input('Deseja sair [s/n]: ')
           if op2.lower() == 's':
               break
               
        elif op1 == 'a':
            tarefa = input('Nome da tarefa: ')
            add(tarefa, lista_tarefas, lista_copia, tarefas_removidas)
 
        elif op1 == 'ls':
            listar(lista_tarefas)

        elif op1 == 'd':
            desfazer(lista_tarefas, tarefas_removidas)
            
        elif op1 == 'r':
            refazer(lista_tarefas, lista_copia)
            tarefas_removidas.clear()
        else:
            print('Opção inválida !! Digite novamente.')

if __name__ == '__main__':
    main()
    
