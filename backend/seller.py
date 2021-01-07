from backend.funcoes import escrever_arquivo, log, read_seller_file

def create_seller(seller):
    dado = f'{seller.get("nome")}*{seller.get("email")}*{seller.get("telefone")}'
    escrever_arquivo(dado, 'seller', 'a')
    log('Created Seller')
    

def seller_list() -> list:
    sellers_list = read_seller_file()
    log('Listed Seller')
    return sellers_list