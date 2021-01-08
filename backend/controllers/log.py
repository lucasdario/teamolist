import datetime as datetime
ROOT = 'backend/arquivos/'


def create_log(valor: str):
    arquivo = open(f'{ROOT}log.txt', 'a')
    data = datetime.datetime.now()
    arquivo.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => {valor}\n"))
    arquivo.close()
    

def list_logs() -> list:
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
