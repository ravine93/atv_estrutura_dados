# lista e dicionario
# id para tarefa (gerar automaticamente) + texto para descrição da tarefa
# status da tarefa: pendente ou concluida
#   novas tarefas devem ter o status "pendente" por padrão
# Menu: adicionar novas tarefas // listar todas as tarefas (incluindo ID + descrição) - devolver msg de erro caso não haja tarefas //
# marcar tarefa como concluída - impedir o user em caso de tarefa inexistente ou já concluída // sair 

tarefas = []
codigo_id = 0

def id_iteravel():
    global codigo_id
    codigo_id += 1
    return codigo_id

def criar_tarefa():
    valor_id = id_iteravel()
    valor_descricao = input(" Descreva tarefa: ")
    valor_status = "Pendente"
    return {
        'id' : valor_id, 
        'descricao' : valor_descricao, 
        'status' : valor_status
        }



while True:
    print(" =========== Menu ===========")
    print(" [1] --> Cadastrar nova tarefa")
    print(" [2] --> Listar tarefas cadastradas")
    print(" [3] --> Concluir tarefa")
    print(" [4] --> Sair")
    
    opcao = input(" Informe o numero referente à sua escolha: ")
    
    if opcao == '1':
        nova_tarefa = criar_tarefa()     
        tarefas.append(nova_tarefa)
        print(f" Tarefa cadastrada no ID: {nova_tarefa['id']}")
            
    elif opcao == '2':
        if tarefas:
            for tarefa in tarefas:
                print(f" ID: {tarefa['id']} --> {tarefa['descricao']}\n Status: {tarefa['status']}")
        else: 
            print(" Erro: nenhuma tarefa cadastrada!")
            
    elif opcao == '3':
        id_busca = int(input(" Informe o ID da tarefa que deseja marcar como concluída: "))
        tarefa_encontrada = None
        for tarefa in tarefas:
            if tarefa['id'] == id_busca:
                tarefa_encontrada = tarefa
                break
            else:
                print(f" Erro: tarefa com o ID {id_busca} não encontrada!")
        if tarefa_encontrada:
            if tarefa_encontrada['status'] == 'Pendente':
                tarefa_encontrada['status'] = 'Concluída'
                print(f" Tarefa com ID: {id_busca} marcada como concluída!")
            else:
                print( " Erro: tarefa já concluída!")
                
    elif opcao == '4':
        print(" Saindo...")
        break
    
    else:
        print(" Erro: opção inválida!")
                    