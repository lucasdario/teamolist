from backend.dao.txt.txt_utils import read_from_txt_file, write_to_txt_file
from backend.controllers.log import create_log


def write_category(form_data: dict):
    name = form_data['nome']
    description = form_data['descricao']
    data_str = f'{name}*{description}'
    write_to_txt_file('list_category.txt', data_str)
    create_log('Created Category')


def read_categories() -> list:
    categories = read_from_txt_file('list_category.txt', ['name', 'description'])
    create_log('Listed Categories')
    return categories
