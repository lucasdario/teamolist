from backend.funcoes import read_from_txt_file


def list_marketplaces() -> list:
    marketplaces = read_from_txt_file('list_marketplace', ['name', 'description'])
    return marketplaces
