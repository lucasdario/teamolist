from backend.funcoes import read_from_txt_file


def product_list() -> list:
    products_list = read_from_txt_file('list_produto')
    return products_list
