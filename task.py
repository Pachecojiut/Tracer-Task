import argparse
import json
from datetime import datetime

# Função para carregar as tarefas do arquivo JSON
def load_tasks():
    try:
        with open('task.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open('task.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# Argumentos da linha de comando
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')
add_parser = subparsers.add_parser('add')
add_parser.add_argument('description')

#Comandos do Usuário
update_parser = subparsers.add_parser('update')
update_parser.add_argument('id', type=int)
update_parser.add_argument('description')

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('id', type=int)

mark_parser = subparsers.add_parser('mark')
mark_parser.add_argument('id', type=int)
mark_parser.add_argument('status', choices=['done', 'todo', 'in-progress'])

list_parser = subparsers.add_parser('list')
list_parser.add_argument('status', nargs='?', default=None, choices=['done', 'todo', 'in-progress'])

args = parser.parse_args()
#Funções dos comandos dos argumentos, Jesus, me ajuda
def update_task(task_id, new_description):
    tasks = load_tasks()  #←←←←A função carrega a tarefa no arquivo JSON
    for task in tasks:    #←←←←Passa por cada tarefa na lista de tarefas
        if task['id'] == task_id: #←←←←←Proucura o ID da tarefa que o usuário quer atualizar
            task['description'] = new_description #←←←←←←Atualiza a descrição da tarefa com a nova descrição fornecida pelo usuário
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #←←←←Atualiza a data de atualização da tarefa com a data e hora atual
            save_tasks(tasks) #←←←←←←Salva a tarefa atualizada no arquivo JSON
            print(f'Task update successfully!') #←←←←Mensagem de sucesso quando ocorre a atualização da tarefa
            print(f'UpdateAt: {task["updatedAt"]}')
            return True
    print(f'Task with ID {task_id} not found.') #←←←←Mensagem de erro adicionada em mark, update, delete.Caso não encontrada a tarefa
    return False

def add_task(description):
    tasks = load_tasks()
    if tasks:
        new_id = max(task['id'] for task in tasks) + 1
    else:
        new_id = 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task= {'id': new_id, 'description': description, 'status': 'todo', 'createdAt': now, 'updatedAt': None}
    tasks.append(task)
    save_tasks(tasks)

def delete_task(task_id):
    tasks = load_tasks()
    original_length=len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == original_length:
        print(f'Task with ID {task_id} not found.') 
        return False
    save_tasks(tasks)
    return True

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            return True
    print(f'Task with ID {task_id} not found.')
    return False

def list_tasks(task_filter=None):
    tasks =load_tasks()
    for task in tasks:
        if task_filter is None or task['status'] == task_filter:
            print(f'ID: {task["id"]}, Description: {task["description"]}, Status: {task["status"]}, CreatedAt: {task["createdAt"]}')
            if task['updatedAt'] is not None:
                print(f'UpdatedAt: {task["updatedAt"]}')
#Condições com as funções dos comandos dos argumentos
if args.command == 'update':
    update_task(args.id, args.description)
elif args.command == 'delete':
    delete_task(args.id)
elif args.command == 'add':
    add_task(args.description)
elif args.command == 'mark':
    mark_task(args.id, args.status)
elif args.command == 'list':
    list_tasks(args.status)








