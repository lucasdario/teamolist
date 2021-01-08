from backend.funcoes import escrever_arquivo, read_from_txt_file
from backend.controllers.log import create_log


def create_product(form_data):
    name = form_data["nome"]
    description = form_data["descricao"]
    price = form_data["preco"]
    data_str = f'{name}*{description}*{price}'
    escrever_arquivo(data_str, 'product', 'a')
    create_log('Created Product')
    
def list_products() -> list:
    products_list = read_from_txt_file('list_product', ['name', 'description', 'price'])
    create_log('Listed Products')
    return products_list


