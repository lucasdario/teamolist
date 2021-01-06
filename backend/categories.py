from backend.funcoes import read_from_txt_file

def list_categories() -> list:
    categories = read_from_txt_file('list_category')
    return categories