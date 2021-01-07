from backend.funcoes import read_from_txt_file


def list_product() -> list:
    products_list = read_from_txt_file('list_product', ['name', 'description', 'price'])
    return products_list
