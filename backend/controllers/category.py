from backend.funcoes import escrever_arquivo, read_from_txt_file
from backend.controllers.log import create_log


def create_category(form_data: dict):
    name = form_data['nome']
    description = form_data['descricao']
    data_str = f'{name}*{description}'
    escrever_arquivo(data_str, 'category', 'a')
    create_log('Created Category')


def list_categories() -> list:
    categories = read_from_txt_file('list_category', ['name', 'description'])
    create_log('Listed Categories')
    return categories
