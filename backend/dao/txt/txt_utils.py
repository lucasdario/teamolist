import datetime as datetime
ROOT = 'backend/arquivos/'


def write_to_txt_file(file_name: str, content: str) -> bool:
    with open(f'{ROOT}{file_name}', 'a') as file:
        try:
            file.write(f'{content}\n')
            return True
        except Exception as e:
            return False
        finally:
            file.close()


def read_from_txt_file(file_name: str, fields: list):
    data_list = []
    with open(f'{ROOT}{file_name}', 'r') as file:
        for line in file:
            line = line.strip().strip('%').split('*')
            data = dict()
            for i, field in enumerate(fields):
                data[field] = line[i]
            data_list.append(data)
    return data_list


def write_log_to_txt_file(content: str):
    arquivo = open(f'{ROOT}log.txt', 'a')
    data = datetime.datetime.now()
    arquivo.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => {content}\n"))
    arquivo.close()
    

def read_logs_from_txt_file() -> list:
    log_list = []
    with open(f'{ROOT}log.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if 'Listed' in line:
                line = {'data': line, 'type': 'list'}
            elif 'Created' in line:
                line = {'data': line, 'type': 'create'}
            log_list.append(line)
    return log_list
