import datetime as datetime
import sys
sys.path.append('.')
ROOT = 'backend/arquivos/'


def escrever_arquivo(valor: str, tipo: str, operador: str) -> bool:
    arquivo = ''
    if tipo == 'marketplace':
        arquivo = open(f'{ROOT}list_marketplace.txt', operador)
    elif tipo == 'product':
        arquivo = open(f'{ROOT}list_product.txt', operador)
    elif tipo == 'seller':
        arquivo = open(f'{ROOT}list_seller.txt', operador)
    elif tipo == 'category':
        arquivo = open(f'{ROOT}list_category.txt', operador)
    try:
        arquivo.write(str(valor)+'%\n')
        return True
    except Exception as e:
        return False
    finally:
        arquivo.close()


def log(valor: str):
    arquivo = open(f'{ROOT}log.txt', 'a')
    data = datetime.datetime.now()
    arquivo.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => Acesso a função {valor}\n"))
    arquivo.close()


def read_from_txt_file(file_name: str, fields: list):
    data_list = []
    with open(f'{ROOT}{file_name}.txt') as file:
        for line in file:
            line = line.strip().strip('%').split('*')
            data = dict()
            for i, field in enumerate(fields):
                data[field] = line[i]
            data_list.append(data)
    file.close()
    log('read_from_txt_file')
    return data_list
