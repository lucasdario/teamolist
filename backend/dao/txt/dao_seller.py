from backend.dao.txt.txt_utils import read_from_txt_file, write_to_txt_file
from backend.controllers.log import create_log


def write_seller(form_data):
    name = form_data["nome"]
    email = form_data["email"]
    phone = form_data["telefone"]
    data_str = f'{name}*{email}*{phone}'
    write_to_txt_file('list_seller.txt', data_str)
    create_log('Created Seller')
    

def read_sellers() -> list:
    sellers = read_from_txt_file('list_seller.txt', ['name', 'email', 'telefone'])
    create_log('Listed Seller')
    return sellers
