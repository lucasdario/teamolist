from backend.funcoes import log, read_from_txt_file


def list_marketplaces() -> list:
    marketplaces = read_from_txt_file('list_marketplace', ['name', 'description'])
    log('Listed Marketplaces')
    return marketplaces
