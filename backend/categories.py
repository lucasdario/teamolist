from backend.funcoes import escrever_arquivo, log, read_from_txt_file


def list_categories() -> list:
    categories = read_from_txt_file('list_category')
    log('Listed Categories')
    return categories


def create_category(form_data: dict):
    name = form_data['nome']
    description = form_data['descricao']
    data_str = f'{name}*{description}'
    escrever_arquivo(data_str, 'category', 'a')
    log('Created Category')
