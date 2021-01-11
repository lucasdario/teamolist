from backend.dao.txt.txt_utils import read_from_txt_file, write_to_txt_file
from backend.controllers.log import create_log


def write_product(form_data):
    name = form_data["nome"]
    description = form_data["descricao"]
    price = form_data["preco"]
    data_str = f'{name}*{description}*{price}'
    write_to_txt_file('list_product.txt', data_str)
    create_log('Created Product')


def read_products() -> list:
    products_list = read_from_txt_file(
        'list_product.txt', ['name', 'description', 'price'])
    for product in products_list:
        product['price'] = float(product['price'])
    create_log('Listed Products')
    return products_list
