from backend.funcoes import escrever_arquivo, read_from_txt_file
from backend.controllers.log import create_log


def create_marketplace(form_data):
    name = form_data["nome"]
    description = form_data["descricao"]
    data_str = f'{name}*{description}'
    escrever_arquivo(data_str, 'marketplace', 'a')
    create_log('Created Marketplace')
    

def list_marketplaces() -> list:
    marketplaces = read_from_txt_file('list_marketplace', ['name', 'description'])
    create_log('Listed Marketplaces')
    return marketplaces
