# Lista de Tarefas Django

Este é um projeto Django simples para gerenciar tarefas (CRUD e pesquisa).

## Requisitos

- Python 3.10+
- Git

## Passos para rodar

1. **Clonar repositório**  
   ```bash
   git clone https://github.com/JoaoM9081/TodoList.git
   cd seu-repo-todo
   ```

2. **Criar e ativar ambiente virtual**  
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate   
   ```

3. **Instalar dependências**  
   ```bash
   python -m pip install django
   ```

4. **Migrar banco de dados**  
   ```bash
   cd todoApp
   python manage.py migrate
   ```

5. **Executar servidor**  
   ```bash
   python manage.py runserver
   ```

7. **Acessar**  
   Abra no navegador `http://127.0.0.1:8000/`

---

Pronto! A partir daqui você já pode criar, editar, buscar e excluir tarefas conforme definido no código.