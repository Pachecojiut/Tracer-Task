import argparse
import json

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')
add_parser = subparsers.add_parser('add')
add_parser.add_argument('description')
args = parser.parse_args()

#Comandos do Usuário
update_parser = subparsers.add_parser('update')
update_parser.add_argument('id')
update_parser.add_argument('description')

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('id')

mark_parser = subparsers.add_parser('mark')
mark_parser.add_argument('id')
mark_parser.add_argument('status')

list_parser = subparsers.add_parser('list')

args = parser.parse_args()
if args.command == 'add':
     with open('task.json', 'r') as f:
        tasks = json.load(f)

if tasks:
    new_id = max(task['id'] for task in tasks) + 1
else:
     new_id = 1
            
task = { 'id': new_id, 'description': args.description, 'status': 'todo' }

    
tasks.append(task)

with open('task.json', 'w') as f:
    json.dump(tasks, f, indent=4)





