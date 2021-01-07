from backend.funcoes import escrever_arquivo, read_from_txt_file

def create_seller(seller):
    dado = f'{seller.get("nome")}*{seller.get("email")}*{seller.get("telefone")}'
    escrever_arquivo(dado, 'seller', 'a')

def seller_list() -> list:
    sellers_list = read_from_txt_file('list_seller', ['name', 'email', 'telefone'])
    return sellers_list