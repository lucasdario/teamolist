from backend.funcoes import escrever_arquivo, read_from_txt_file
from backend.controllers.log import create_log


def create_seller(form_data):
    name = form_data["nome"]
    email = form_data["email"]
    phone = form_data["telefone"]
    data_str = f'{name}*{email}*{phone}'
    escrever_arquivo(data_str, 'seller', 'a')
    create_log('Created Seller')
    

def list_sellers() -> list:
    sellers = read_from_txt_file('list_seller', ['name', 'email', 'telefone'])
    create_log('Listed Seller')
    return sellers
