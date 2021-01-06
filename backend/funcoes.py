import datetime as datetime
import sys
sys.path.append('.')
ROOT = 'backend/arquivos/'


def escrever_arquivo(valor: str, tipo: int, operador: str) -> bool:
    arquivo = ''
    if tipo == 0:
        arquivo = open(f'{ROOT}list_marketplace.txt', operador)
    elif tipo == 1:
        arquivo = open(f'{ROOT}list_produto.txt', operador)
    elif tipo == 2:
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


def read_from_txt_file(file_name: str):
    data_list = []
    with open(f'{ROOT}{file_name}.txt') as file:
        for line in file:
            line = line.strip().strip('%').split('*')
            data = {'name': line[0], 'description': line[1]}
            if file_name == 'list_produto':
                data['price'] = line[2]
            data_list.append(data)
    
    return data_list
            