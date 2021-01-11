from backend.dao.txt.txt_utils import read_from_txt_file, write_to_txt_file
from backend.controllers.log import create_log


def write_marketplace(form_data):
    name = form_data["nome"]
    description = form_data["descricao"]
    data_str = f'{name}*{description}'
    write_to_txt_file('list_marketplace.txt', data_str)
    create_log('Created Marketplace')
    

def read_marketplaces() -> list:
    marketplaces = read_from_txt_file('list_marketplace.txt', ['name', 'description'])
    create_log('Listed Marketplaces')
    return marketplaces
