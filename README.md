# Tracer Task

Gerenciador de tarefas simples para terminal, desenvolvido em Python.

## Requisitos

* Python 3
* Git

## Instalação

```bash
git clone https://github.com/davi2010pacheco-crypto/Tracer-Task.git
cd Tracer-Task
```

Não é necessário instalar dependências externas.

## Uso

### Adicionar

```bash
python3 task.py add "Estudar Python"
```

### Listar

```bash
python3 task.py list
python3 task.py list todo
python3 task.py list done
python3 task.py list in-progress
```

### Atualizar

```bash
python3 task.py update 1 "Nova descrição"
```

### Alterar status

```bash
python3 task.py mark 1 done
python3 task.py mark 1 in-progress
python3 task.py mark 1 todo
```

### Excluir

```bash
python3 task.py delete 1
```

## Armazenamento

As tarefas são armazenadas localmente no arquivo `task.json`, criado automaticamente quando necessário.

## Projeto

https://github.com/Pachecojiut/Tracer-Task/tree/master

## Tecnologias

* Python 3
* JSON
* argparse
